import os
import jittor
from jittor import nn
from jittor import optim

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
    cnn, layerList = loadModel(params.model_file, params.pooling, params.gpu)