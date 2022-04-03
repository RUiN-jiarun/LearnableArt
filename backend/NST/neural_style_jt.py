import os
import jittor as jt
from jittor import nn
from jittor import optim
from jittor import transform

from PIL import Image
from models_jt import loadModel

import argparse
parser = argparse.ArgumentParser()
# Basic options
parser.add_argument("-style_image", help="Style target image", default='examples/inputs/the_scream.jpg')
parser.add_argument("-style_blend_weights", default=None)
parser.add_argument("-content_image", help="Content target image", default='examples/inputs/mill.jpg')
parser.add_argument("-image_size", help="Maximum height / width of generated image", type=int, default=700)
parser.add_argument("-gpu", help="Zero-indexed ID of the GPU to use; for CPU mode set -gpu = c", default=0)

# Optimization options
parser.add_argument("-content_weight", type=float, default=5e0)
parser.add_argument("-style_weight", type=float, default=1e2)
parser.add_argument("-normalize_weights", action='store_true')
parser.add_argument("-normalize_gradients", action='store_true')
parser.add_argument("-tv_weight", type=float, default=1e-4)
parser.add_argument("-num_iterations", type=int, default=1000)
parser.add_argument("-init", choices=['random', 'image'], default='image')
parser.add_argument("-init_image", default=None)
parser.add_argument("-optimizer", choices=['lbfgs', 'adam'], default='lbfgs')
parser.add_argument("-learning_rate", type=float, default=1e0)
parser.add_argument("-lbfgs_num_correction", type=int, default=100)
parser.add_argument("-improve_gram", action='store_true')

# Output options
parser.add_argument("-print_iter", type=int, default=100)
parser.add_argument("-save_iter", type=int, default=200)
parser.add_argument("-output_image", default='out.png')

# Other options
parser.add_argument("-style_scale", type=float, default=1.0)
parser.add_argument("-original_colors", type=int, choices=[0, 1], default=0)
parser.add_argument("-pooling", choices=['avg', 'max'], default='max')
parser.add_argument("-model_file", type=str, default='models/vgg19.pkl')
parser.add_argument("-backend", choices=['nn', 'cudnn', 'mkl', 'mkldnn', 'openmp', 'mkl,cudnn', 'cudnn,mkl'], default='cudnn')
parser.add_argument("-cudnn_autotune", action='store_true')
parser.add_argument("-seed", type=int, default=-1)
parser.add_argument("-plot", action='store_true')

parser.add_argument("-content_layers", help="layers for content", default='relu4_2')
# parser.add_argument("-style_layers", help="layers for style", default='relu1_1,relu2_1,relu3_1,relu4_1,relu5_1')
# Improvement 2
# Use all layers for style feature extraction and reconstruction
parser.add_argument("-style_layers", help="layers for style", default='relu1_1,relu1_2,relu2_1,relu2_2,relu3_1,relu3_2,relu3_3,relu3_4,relu4_1,relu4_2,relu4_3,relu4_4,relu5_1,relu5_2,relu5_3,relu5_4')
# parser.add_argument("-style_layers", help="layers for style", default='conv1_1,conv1_2,conv2_1,conv2_2,conv3_1,conv3_2,conv3_3,conv3_4,conv4_1,conv4_2,conv4_3,conv4_4,conv5_1,conv5_2,conv5_3,conv5_4')


parser.add_argument("-multidevice_strategy", default='4,7,29')
params = parser.parse_args()


def main():
    dtype, multidevice, backward_device = setup_gpu()

    cnn, layerList = loadModel(params.model_file, params.pooling, params.gpu)

    content_image = preprocess(params.content_image, params.image_size)
    # print(content_image)
    style_image_input = params.style_image.split(',')
    style_image_list, ext = [], [".jpg", ".jpeg", ".png", ".tiff"]
    for image in style_image_input:
        if os.path.isdir(image):
            images = (image + "/" + file for file in os.listdir(image)
            if os.path.splitext(file)[1].lower() in ext)
            style_image_list.extend(images)
        else:
            style_image_list.append(image)
    style_images_caffe = []
    for image in style_image_list:
        style_size = int(params.image_size * params.style_scale)
        img_caffe = preprocess(image, style_size)
        style_images_caffe.append(img_caffe)
    
    if params.init_image != None:
        image_size = (content_image.size(2), content_image.size(3))
        init_image = preprocess(params.init_image, image_size)
    
    style_blend_weights = []
    if params.style_blend_weights == None:
        # Style blending not specified, so use equal weighting
        for i in style_image_list:
            style_blend_weights.append(1.0)
        for i, blend_weights in enumerate(style_blend_weights):
            style_blend_weights[i] = int(style_blend_weights[i])
    else:
        style_blend_weights = params.style_blend_weights.split(',')
        assert len(style_blend_weights) == len(style_image_list), \
          "-style_blend_weights and -style_images must have the same number of elements!"
    style_blend_sum = 0
    for i, blend_weights in enumerate(style_blend_weights):
        style_blend_weights[i] = float(style_blend_weights[i])
        style_blend_sum = float(style_blend_sum) + style_blend_weights[i]
    for i, blend_weights in enumerate(style_blend_weights):
        style_blend_weights[i] = float(style_blend_weights[i]) / float(style_blend_sum)

    content_layers = params.content_layers.split(',')
    style_layers = params.style_layers.split(',')

    print(cnn)




def setup_gpu():
    def setup_cuda():
        jt.flags.use_cuda = 1

    def setup_cpu():
        jt.flags.use_cuda = 0
    
    multidevice = False
    if "," in str(params.gpu):
        devices = params.gpu.split(',')
        multidevice = True

        if 'c' in str(devices[0]).lower():
            backward_device = "cpu"
            setup_cuda()
        else:
            backward_device = "cuda:" + devices[0]
            setup_cpu()
        dtype = jt.Var

    elif "c" not in str(params.gpu).lower():
        setup_cuda()
        dtype, backward_device = jt.Var, "cuda:" + str(params.gpu)
    else:
        setup_cpu()
        dtype, backward_device = jt.Var, "cpu"
    return dtype, multidevice, backward_device

def preprocess(image_name, image_size):
    image = Image.open(image_name).convert('RGB')
    if type(image_size) is not tuple:
        image_size = tuple([int((float(image_size) / max(image.size))*x) for x in (image.height, image.width)])
    Loader = transform.Compose([transform.Resize(image_size), transform.ToTensor()])
    rgb2bgr = transform.Compose([transform.Lambda(lambda x: x[jt.int32([2,1,0])])])
    Normalize = transform.Compose([transform.ImageNormalize(mean=[103.939, 116.779, 123.68], std=[1,1,1])])
    tensor = jt.unsqueeze(Normalize(rgb2bgr(Loader(image) * 255)), dim=0)
    return tensor
    # return a numpy.ndarray

def deprocess(output_tensor):
    Normalize = transform.Compose([transform.ImageNormalize(mean=[-103.939, -116.779, -123.68], std=[1,1,1])])
    bgr2rgb = transform.Compose([transform.Lambda(lambda x: x[jt.int32([2,1,0])])])
    output_tensor = bgr2rgb(Normalize(jt.squeeze(output_tensor, dim=0))) / 255
    output_tensor = output_tensor.clamp(0, 1)
    Image2PIL = transform.ToPILImage()
    image = Image2PIL(output_tensor)
    return image

if __name__ == "__main__":
    main()