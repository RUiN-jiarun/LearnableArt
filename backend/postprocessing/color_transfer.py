import argparse
import os
import numpy as np

# scipy must below 1.3.0
# from scipy.misc import imread, imresize, imsave, fromimage, toimage
from .utils import imread, imresize, imsave, fromimage, toimage


# Util function to match histograms
def match_histograms(source, template):

    oldshape = source.shape
    source = source.ravel()
    template = template.ravel()

    # get the set of unique pixel values and their corresponding indices and
    # counts
    s_values, bin_idx, s_counts = np.unique(source, return_inverse=True,
                                            return_counts=True)
    t_values, t_counts = np.unique(template, return_counts=True)

    # take the cumsum of the counts and normalize by the number of pixels to
    # get the empirical cumulative distribution functions for the source and
    # template images (maps pixel value --> quantile)
    s_quantiles = np.cumsum(s_counts).astype(np.float64)
    s_quantiles /= s_quantiles[-1]
    t_quantiles = np.cumsum(t_counts).astype(np.float64)
    t_quantiles /= t_quantiles[-1]

    # interpolate linearly to find the pixel values in the template image
    # that correspond most closely to the quantiles in the source image
    interp_t_values = np.interp(s_quantiles, t_quantiles, t_values)

    return interp_t_values[bin_idx].reshape(oldshape)


# util function to preserve image color
def original_color_transform(content, generated, mask=None, hist_match=0, mode='YCbCr'):
    generated = np.asarray(toimage(generated, mode='RGB'))
    # FIXME
    generated.convert('YCbCr')  # Convert to YCbCr color space

    if mask is None:
        if hist_match == 1:
            for channel in range(3):
                generated[:, :, channel] = match_histograms(generated[:, :, channel], content[:, :, channel])
        else:
            generated[:, :, 1:] = content[:, :, 1:]
    else:
        width, height, channels = generated.shape

        for i in range(width):
            for j in range(height):
                if mask[i, j] == 1:
                    if hist_match == 1:
                        for channel in range(3):
                            generated[i, j, channel] = match_histograms(generated[i, j, channel], content[i, j, channel])
                    else:
                        generated[i, j, 1:] = content[i, j, 1:]

    generated = np.asarray(toimage(generated, mode=mode))  # Convert to RGB color space
    return generated


# util function to load masks
def load_mask(mask_path, shape):
    mask = imread(mask_path, mode="L") # Grayscale mask load
    width, height, _ = shape
    mask = imresize(mask, (width, height), interp='bicubic').astype('float32')

    # Perform binarization of mask
    mask[mask <= 127] = 0
    mask[mask > 128] = 255

    mask /= 255
    mask = mask.astype(np.int32)

    return mask


# parser = argparse.ArgumentParser(description='Neural style transfer color preservation.')

# parser.add_argument('content_image', type=str, help='Path to content image')
# parser.add_argument('generated_image', type=str, help='Path to generated image')
# parser.add_argument('--mask', default=None, type=str, help='Path to mask image')
# parser.add_argument('--hist_match', type=int, default=0, help='Perform histogram matching for color matching')

# args = parser.parse_args()

def color_trans(generated_image, content_image, mask, hist_match):
    if hist_match == 1:
        # image_suffix = "_color.png"
        mode = "RGB"
    else:
        # image_suffix = "_color.png"
        mode = "YCbCr"
    # mode = hist_match

    image_path = os.path.splitext(generated_image)[0] + "_color.png"

    generated_image = imread(generated_image, mode="RGB")
    img_width, img_height, _ = generated_image.shape

    content_image = imread(content_image, mode=mode)
    content_image = imresize(content_image, (img_width, img_height), interp='bicubic')

    if mask == 1:
        mask_img = load_mask(mask, generated_image.shape)
    else:
        mask_img = None

    img = original_color_transform(content_image, generated_image, mask_img, hist_match, mode=mode)

    # return img
    imsave(image_path, img)

    # print("Image saved at path : %s" % image_path)



