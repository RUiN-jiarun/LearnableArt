import os
import copy
import jittor as jt
from jittor import nn
from jittor import optim
from jittor import transform
# FUCK.
from torch.optim import LBFGS
import torch
# from lbfgs_jt import LBFGS

from PIL import Image
from .models_jt import loadModel

import argparse
parser = argparse.ArgumentParser()
# Basic options
parser.add_argument("-style_image", help="Style target image", default='examples/inputs/starry_night.jpg')
parser.add_argument("-style_blend_weights", default=None)
parser.add_argument("-content_image", help="Content target image", default='examples/inputs/bird.png')
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
parser.add_argument("-optimizer", choices=['lbfgs', 'adam'], default='adam')
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
parser.add_argument("-model_file", type=str, default='NST/models/vgg19-d01eb7cb.pth')   # NST/models/vgg19-d01eb7cb.pth
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

def param_main(content_image, style_image, output_image):
    params.content_image = content_image
    params.style_image = style_image
    params.output_image = output_image
    # print(params)
    main()
    # TODO: Memory collection
    jt.sync_all()
    jt.gc()
    print('Done.')


def main():
    jt.flags.use_cuda = 1
    jt.cudnn.set_max_workspace_ratio(0.0)

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

    # print(cnn)
    cnn = copy.deepcopy(cnn)
    content_losses, style_losses, tv_losses = [], [], []
    next_content_idx, next_style_idx = 1, 1
    net = nn.Sequential()
    c, r = 0, 0
    if params.tv_weight > 0:
        tv_mod = TVLoss(params.tv_weight)
        net.add_module(str(len(net)), tv_mod)
        tv_losses.append(tv_mod)

    for i, layer in enumerate(list(cnn), 1):
        if next_content_idx <= len(content_layers) or next_style_idx <= len(style_layers):
            if isinstance(layer, nn.Conv2d):
                net.add_module(str(len(net)), layer)

                if layerList['C'][c] in content_layers:
                    print("Setting up content layer " + str(i) + ": " + str(layerList['C'][c]))
                    loss_module = ContentLoss(params.content_weight, params.normalize_gradients)
                    net.add_module(str(len(net)), loss_module)
                    content_losses.append(loss_module)
                
                # TODO: Add chained inference
                if layerList['C'][c] in style_layers:
                    print("Setting up style layer " + str(i) + ": " + str(layerList['C'][c]))
                    loss_module = StyleLoss(params.style_weight)
                    net.add_module(str(len(net)), loss_module)
                    style_losses.append(loss_module)
                c+=1

            if isinstance(layer, nn.ReLU):
                net.add_module(str(len(net)), layer)

                if layerList['R'][r] in content_layers:
                    print("Setting up content layer " + str(i) + ": " + str(layerList['R'][r]))
                    loss_module = ContentLoss(params.content_weight)
                    net.add_module(str(len(net)), loss_module)
                    content_losses.append(loss_module)
                    next_content_idx += 1

                if layerList['R'][r] in style_layers:
                    print("Setting up style layer " + str(i) + ": " + str(layerList['R'][r]))
                    loss_module = StyleLoss(params.style_weight)
                    net.add_module(str(len(net)), loss_module)
                    style_losses.append(loss_module)
                    next_style_idx += 1
                r+=1

            if isinstance(layer, nn.MaxPool2d) or isinstance(layer, nn.AvgPool2d):
                net.add_module(str(len(net)), layer)
    # print(net)

    # Capture content targets
    for i in content_losses:
        i.mode = 'capture'
    print("Capturing content targets")
    # print_torch(net, multidevice)         # TODO: print like torch
    net(jt.Var(content_image))
    # print(content_losses)

    # Capture style targets
    for i in content_losses:
        i.mode = 'None'

    for i, image in enumerate(style_images_caffe):
        print("Capturing style target " + str(i+1))
        for j in style_losses:
            j.mode = 'capture'
            j.blend_weight = style_blend_weights[i]
        net(jt.Var(style_images_caffe[i]))
    
    # Set all loss modules to loss mode
    for i in content_losses:
        i.mode = 'loss'
    for i in style_losses:
        i.mode = 'loss'

    # TODO: Freeze the network in order to prevent
    # unnecessary gradient calculations
    for param in net.parameters():
        param.requires_grad = False
    
    # Initialize the image
    # if params.seed >= 0:
    #     jt.manual_seed(params.seed)
    #     jt.cuda.manual_seed_all(params.seed)
    #     jt.backends.cudnn.deterministic=True
    if params.init == 'random':
        B, C, H, W = content_image.shape
        img = jt.randn(C, H, W).multiply(0.001).unsqueeze(0)
    elif params.init == 'image':
        if params.init_image != None:
            img = jt.Var(init_image).clone()
        else:
            img = jt.Var(content_image).clone()
    img = nn.Parameter(img)
    # print(img)

    def maybe_print(t, loss):
        if params.print_iter > 0 and t % params.print_iter == 0:
            print("Iteration " + str(t) + " / "+ str(params.num_iterations))
            for i, loss_module in enumerate(content_losses):
                print("  Content " + str(i+1) + " loss: " + str(loss_module.loss.item()))
            for i, loss_module in enumerate(style_losses):
                print("  Style " + str(i+1) + " loss: " + str(loss_module.loss.item()))
            print("  Total loss: " + str(loss.item()))

    def maybe_save(t):
        should_save = params.save_iter > 0 and t % params.save_iter == 0
        should_save = should_save or t == params.num_iterations
        if should_save:
            output_filename, file_extension = os.path.splitext(params.output_image)
            if t == params.num_iterations:
                filename = output_filename + str(file_extension)
            else:
                filename = str(output_filename) + "_" + str(t) + str(file_extension)
            disp = deprocess(img.clone())

            # Maybe perform postprocessing for color-independent style transfer
            # if params.original_colors == 1:
            #     disp = original_colors(deprocess(content_image.clone()), disp)

            disp.save(str(filename))
    
    # Function to evaluate loss and gradient. We run the net forward and
    # backward to get the gradient, and sum up losses from the loss modules.
    # optim.lbfgs internally handles iteration and calls this function many
    # times, so we manually count the number of iterations to handle printing
    # and saving intermediate results.
    num_calls = [0]

    # # Initialize params for plot
    loss_list = []

    def feval():
        num_calls[0] += 1
        optimizer.zero_grad()
        net(img)
        loss = 0

        for mod in content_losses:
            # print(mod.loss.data)
            loss += torch.tensor(mod.loss.data).to('cuda:0').requires_grad_()
        for mod in style_losses:
            # print(mod)
            loss += torch.tensor(mod.loss.data).to('cuda:0').requires_grad_()
            # jt.gc()
        if params.tv_weight > 0:
            for mod in tv_losses:
                loss += torch.tensor(mod.loss.data).to('cuda:0').requires_grad_()
        # print(loss)
        # TODO: requires_grad
        # loss = torch.tensor(loss.data)
        loss.requires_grad_()
        loss.backward()

        maybe_save(num_calls[0])
        maybe_print(num_calls[0], loss)

        # loss_list.append(loss)

        return loss

    optimizer, loopVal = setup_optimizer(img)
    if params.optimizer == 'lbfgs':
        while num_calls[0] <= loopVal:
            optimizer.step(feval)
            # jt.gc()
    else: 
        while num_calls[0] <= loopVal:
            # optimizer.step(feval)
            num_calls[0] += 1
            optimizer.zero_grad()
            net(img)
            loss = 0

            for mod in content_losses:
                loss += mod.loss
            for mod in style_losses:
                loss += mod.loss
            if params.tv_weight > 0:
                for mod in tv_losses:
                    loss += mod.loss

            
            optimizer.backward(loss)
            optimizer.step()
            # jt.gc()
            maybe_save(num_calls[0])
            maybe_print(num_calls[0], loss)


# Configure the optimizer
def setup_optimizer(img):
    if params.optimizer == 'lbfgs':
        print("Running optimization with L-BFGS")
        optim_state = {
            'max_iter': params.num_iterations,
            'tolerance_change': -1,
            'tolerance_grad': -1,
        }
        if params.lbfgs_num_correction != 100:
            optim_state['history_size'] = params.lbfgs_num_correction
        optimizer = LBFGS([torch.tensor(img.data)], **optim_state)
        loopVal = 1
    elif params.optimizer == 'adam':
        print("Running optimization with ADAM")
        optimizer = optim.Adam([img], lr = params.learning_rate)
        loopVal = params.num_iterations - 1
    return optimizer, loopVal



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

def deprocess(output):
    Normalize = transform.Compose([transform.ImageNormalize(mean=[-103.939, -116.779, -123.68], std=[1,1,1])])
    bgr2rgb = transform.Compose([transform.Lambda(lambda x: x[jt.int32([2,1,0])])])
    output = bgr2rgb(Normalize(jt.squeeze(output, dim=0))) / 255
    output = output.clamp(0, 1)
    
    # change (H,W,C) to (C,H,W)
    output = output.transpose((1,2,0))
    print(output.ndim)
    Image2PIL = transform.ToPILImage()
    image = Image2PIL(output)
    return image

def test():
    content_image = preprocess(params.content_image, params.image_size)
    # print(jt.Var(content_image))
    img = deprocess(jt.Var(content_image))
    print(img)

class ContentLoss(nn.Module):

    def __init__(self, strength):
        super(ContentLoss, self).__init__()
        self.strength = strength
        self.crit = nn.MSELoss()
        self.mode = 'None'

    def execute(self, x):
        if self.mode == 'loss':
            loss = self.crit(x, self.target)
            self.loss = loss * self.strength
        elif self.mode == 'capture':
            self.target = x.detach()
        return x

class GramMatrix(nn.Module):

    def execute(self, x):
        B, C, H, W = x.size()
        x_flat = x.view(C, H * W)
        # Improvement 1
        # The Gram matrix of an image tensor (feature-wise outer product) using shifted activations
        return jt.matmul(x_flat.add(-10), (x_flat.add(-10)).t())

# Improvement: Space Conversion Map Based Gram Matrix 
class ImprovedGramMatrixX(nn.Module):

    def execute(self, x):
        rshift = x[:,:,:,4:]
        lshift = x[:,:,:,:-4]
        B, C, H, W = rshift.size()
        # print(B, C, H, W)
        # x_flat = x.view(C, H * W)   # flatten

        l_flat = lshift.contiguous().view(C, H * W)
        r_flat = rshift.contiguous().view(C, H * W)

        return jt.matmul(l_flat.add(-5), r_flat.add(-5).t())

class ImprovedGramMatrixY(nn.Module):

    def execute(self, x):
        dshift = x[:,:,4:,:]
        ushift = x[:,:,:-4,:]
        B, C, H, W = ushift.size()

        # x_flat = x.view(C, H * W)   # flatten

        d_flat = dshift.contiguous().view(C, H * W)
        u_flat = ushift.contiguous().view(C, H * W)

        return jt.matmul(u_flat.add(-5), d_flat.add(-5).t())

class StyleLoss(nn.Module):

    def __init__(self, strength):
        super(StyleLoss, self).__init__()
        self.target = jt.Var([])
        self.strength = strength
        self.gram = GramMatrix()

        # Improvement Test
        self.gramx = ImprovedGramMatrixX()
        self.gramy = ImprovedGramMatrixY()

        self.crit = nn.MSELoss()
        self.mode = 'None'
        self.blend_weight = None

    def execute(self, x):
        # Improvement: New Loss Function
        if params.improve_gram:
            self.Gx = self.gramx(x)
            self.Gy = self.gramy(x)

            self.G = 0.5 * (self.Gx + self.Gy)
        else:
            self.G = self.gram(x)

        self.G = self.G.divide(x.numel())
        if self.mode == 'capture':
            if self.blend_weight == None:
                self.target = self.G.detach()
            elif self.target.numel() == 0:
                self.target = self.G.detach().multiply(self.blend_weight)
            else:
                self.target = self.target.add(self.blend_weight, self.G.detach())
        elif self.mode == 'loss':
            loss = self.crit(self.G, self.target)
            self.loss = self.strength * loss
        return x



class TVLoss(nn.Module):

    def __init__(self, strength):
        super(TVLoss, self).__init__()
        self.strength = strength

    def execute(self, x):
        self.x_diff = x[:,:,1:,:] - x[:,:,:-1,:]
        self.y_diff = x[:,:,:,1:] - x[:,:,:,:-1]
        self.loss = self.strength * (jt.sum(jt.abs(self.x_diff)) + jt.sum(jt.abs(self.y_diff)))
        return x


if __name__ == "__main__":
    main()
    # test()