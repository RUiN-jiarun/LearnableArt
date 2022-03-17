
import numpy as np
import imageio
from PIL import Image
from skimage import color
import matplotlib.pyplot as plt
from io import StringIO


def imread(path, mode="RGB"):
    # Loads data in HxW format, then transposes to correct format
    img = np.array(imageio.imread(path, pilmode=mode))
    return img

def imread_gray(path):
    img = np.array(imageio.imread(path, as_gray=True))
    return img

def imresize(img, size, interp='bilinear'):
    """
    Resizes an image

    :param img:
    :param size: (Must be H, W format !)
    :param interp:
    :return:
    """
    if interp == 'bilinear':
        interpolation = Image.BILINEAR
    elif interp == 'bicubic':
        interpolation = Image.BICUBIC
    else:
        interpolation = Image.NEAREST

    # Requires size to be HxW
    size = (size[1], size[0])

    if type(img) != Image:
        img = Image.fromarray(img)
        # img = Image.open(StringIO(img))

    img = np.array(img.resize(size, interpolation))
    return img
    
    
def imsave(path, img):
    imageio.imwrite(path, img)
    return
    

def fromimage(img, mode='RGB'):
    if mode == 'RGB':
        img = color.lab2rgb(img)
    else:
        img = color.rgb2lab(img)
    return img


def toimage(arr, mode='RGB'):
    return Image.fromarray(np.uint8(arr)).convert(mode)

def drawhist(path, savepath):
    src = Image.open(path)
    # print(src.mode)
    if src.mode == 'RGBA':
        r, g, b, a = src.split()
    else:
        r, g, b = src.split()

    xaxis = [i for i in range(0,256)]
    # print(xaxis)
    plt.figure("hist")
    # ar = np.array(r).flatten()
    ar = r.histogram()
    # print(ar)
    plt.bar(xaxis, ar, fc='r')
    # plt.hist(ar, bins=256, density=False, facecolor='r', edgecolor='r')
    # ag = np.array(g).flatten()
    ag = g.histogram()
    plt.bar(xaxis, ag, fc='g')
    # plt.hist(ag, bins=256, density=False, facecolor='g', edgecolor='g')
    # ab = np.array(b).flatten()
    ab = b.histogram()
    plt.bar(xaxis, ab, fc='b')
    # plt.hist(ab, bins=256, density=False, facecolor='b', edgecolor='b')
    plt.savefig(fname=savepath)

if __name__ == '__main__':
    drawhist("shen/bird.png", "shen/bird_hist.png")
    drawhist("shen/farmer_paint.png", "shen/farmer_paint_hist.png")
    drawhist("shen/ancient_totum.jpg", "shen/totum_hist.png")
    drawhist("lena.png", "lena_hist.png")
    drawhist("shen/mountain.jpg", "shen/mountain_hist.png")
    drawhist("shen/picasso_selfport1907.jpg", "shen/picasso_hist.png")