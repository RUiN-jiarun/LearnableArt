import os
import copy
import torch
import torch.nn as nn
import torch.optim as optim
import torchvision.transforms as transforms

from PIL import Image
from models import loadModel, ModelParallel

import matplotlib.pyplot as plt

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
parser.add_argument("-model_file", type=str, default='models/vgg19-d01eb7cb.pth')
parser.add_argument("-disable_check", action='store_true')
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


Image.MAX_IMAGE_PIXELS = 1000000000 # Support gigapixel images


def main():
    dtype, multidevice, backward_device = setup_gpu()

    cnn, layerList = loadModel(params.model_file, params.pooling, params.gpu, params.disable_check)

    content_image = preprocess(params.content_image, params.image_size).type(dtype)
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
        img_caffe = preprocess(image, style_size).type(dtype)
        style_images_caffe.append(img_caffe)

    if params.init_image != None:
        image_size = (content_image.size(2), content_image.size(3))
        init_image = preprocess(params.init_image, image_size).type(dtype)

    # Handle style blending weights for multiple style inputs
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

    # Normalize the style blending weights so they sum to 1
    style_blend_sum = 0
    for i, blend_weights in enumerate(style_blend_weights):
        style_blend_weights[i] = float(style_blend_weights[i])
        style_blend_sum = float(style_blend_sum) + style_blend_weights[i]
    for i, blend_weights in enumerate(style_blend_weights):
        style_blend_weights[i] = float(style_blend_weights[i]) / float(style_blend_sum)

    content_layers = params.content_layers.split(',')
    style_layers = params.style_layers.split(',')

    # Set up the network, inserting style and content loss modules
    # print(cnn)
    cnn = copy.deepcopy(cnn)
    content_losses, style_losses, tv_losses = [], [], []
    next_content_idx, next_style_idx = 1, 1
    net = nn.Sequential()
    c, r = 0, 0
    if params.tv_weight > 0:
        tv_mod = TVLoss(params.tv_weight).type(dtype)
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
                    loss_module = StyleLoss(params.style_weight, params.normalize_gradients)
                    net.add_module(str(len(net)), loss_module)
                    style_losses.append(loss_module)
                c+=1

            if isinstance(layer, nn.ReLU):
                net.add_module(str(len(net)), layer)

                if layerList['R'][r] in content_layers:
                    print("Setting up content layer " + str(i) + ": " + str(layerList['R'][r]))
                    loss_module = ContentLoss(params.content_weight, params.normalize_gradients)
                    net.add_module(str(len(net)), loss_module)
                    content_losses.append(loss_module)
                    next_content_idx += 1

                if layerList['R'][r] in style_layers:
                    print("Setting up style layer " + str(i) + ": " + str(layerList['R'][r]))
                    loss_module = StyleLoss(params.style_weight, params.normalize_gradients)
                    net.add_module(str(len(net)), loss_module)
                    style_losses.append(loss_module)
                    next_style_idx += 1
                r+=1

            if isinstance(layer, nn.MaxPool2d) or isinstance(layer, nn.AvgPool2d):
                net.add_module(str(len(net)), layer)
    # print(net)
    if multidevice:
        net = setup_multi_device(net)

    # Capture content targets
    for i in content_losses:
        i.mode = 'capture'
    print("Capturing content targets")
    print_torch(net, multidevice)
    net(content_image)

    # # Capture style targets
    # for i in content_losses:
    #     i.mode = 'None'

    # for i, image in enumerate(style_images_caffe):
    #     print("Capturing style target " + str(i+1))
    #     for j in style_losses:
    #         j.mode = 'capture'
    #         j.blend_weight = style_blend_weights[i]
    #     net(style_images_caffe[i])

    # # Set all loss modules to loss mode
    # for i in content_losses:
    #     i.mode = 'loss'
    # for i in style_losses:
    #     i.mode = 'loss'

    # # Maybe normalize content and style weights
    # if params.normalize_weights:
    #     normalize_weights(content_losses, style_losses)

    # # Freeze the network in order to prevent
    # # unnecessary gradient calculations
    # for param in net.parameters():
    #     param.requires_grad = False

    # # Initialize the image
    # if params.seed >= 0:
    #     torch.manual_seed(params.seed)
    #     torch.cuda.manual_seed_all(params.seed)
    #     torch.backends.cudnn.deterministic=True
    # if params.init == 'random':
    #     B, C, H, W = content_image.size()
    #     img = torch.randn(C, H, W).mul(0.001).unsqueeze(0).type(dtype)
    # elif params.init == 'image':
    #     if params.init_image != None:
    #         img = init_image.clone()
    #     else:
    #         img = content_image.clone()
    # img = nn.Parameter(img)

    # # Initialize params for plot
    # loss_list = []

    # def maybe_print(t, loss):
    #     if params.print_iter > 0 and t % params.print_iter == 0:
    #         print("Iteration " + str(t) + " / "+ str(params.num_iterations))
    #         for i, loss_module in enumerate(content_losses):
    #             print("  Content " + str(i+1) + " loss: " + str(loss_module.loss.item()))
    #         for i, loss_module in enumerate(style_losses):
    #             print("  Style " + str(i+1) + " loss: " + str(loss_module.loss.item()))
    #         print("  Total loss: " + str(loss.item()))

    # def maybe_save(t):
    #     should_save = params.save_iter > 0 and t % params.save_iter == 0
    #     should_save = should_save or t == params.num_iterations
    #     if should_save:
    #         output_filename, file_extension = os.path.splitext(params.output_image)
    #         if t == params.num_iterations:
    #             filename = output_filename + str(file_extension)
    #         else:
    #             filename = str(output_filename) + "_" + str(t) + str(file_extension)
    #         disp = deprocess(img.clone())

    #         # Maybe perform postprocessing for color-independent style transfer
    #         if params.original_colors == 1:
    #             disp = original_colors(deprocess(content_image.clone()), disp)

    #         disp.save(str(filename))

    # # Function to evaluate loss and gradient. We run the net forward and
    # # backward to get the gradient, and sum up losses from the loss modules.
    # # optim.lbfgs internally handles iteration and calls this function many
    # # times, so we manually count the number of iterations to handle printing
    # # and saving intermediate results.
    # num_calls = [0]
    # def feval():
    #     num_calls[0] += 1
    #     optimizer.zero_grad()
    #     net(img)
    #     loss = 0

    #     for mod in content_losses:
    #         loss += mod.loss.to(backward_device)
    #     for mod in style_losses:
    #         loss += mod.loss.to(backward_device)
    #     if params.tv_weight > 0:
    #         for mod in tv_losses:
    #             loss += mod.loss.to(backward_device)

    #     loss.backward()

    #     maybe_save(num_calls[0])
    #     maybe_print(num_calls[0], loss)

    #     loss_list.append(loss)

    #     return loss

    # optimizer, loopVal = setup_optimizer(img)
    # while num_calls[0] <= loopVal:
    #     optimizer.step(feval)

    # if params.plot:
    #     x1 = range(0, params.num_iterations)
    #     y1 = loss_list
    #     plt.plot(x1, y1)
    #     plt.xlabel('Iters')
    #     plt.ylabel('Total Loss')
    #     plt.show()
    #     # plt.savefig('loss.jpg')   # FIXME: save bug

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
        optimizer = optim.LBFGS([img], **optim_state)
        loopVal = 1
    elif params.optimizer == 'adam':
        print("Running optimization with ADAM")
        optimizer = optim.Adam([img], lr = params.learning_rate)
        loopVal = params.num_iterations - 1
    return optimizer, loopVal


def setup_gpu():
    def setup_cuda():
        if 'cudnn' in params.backend:
            torch.backends.cudnn.enabled = True
            if params.cudnn_autotune:
                torch.backends.cudnn.benchmark = True
        else:
            torch.backends.cudnn.enabled = False

    def setup_cpu():
        if 'mkl' in params.backend and 'mkldnn' not in params.backend:
            torch.backends.mkl.enabled = True
        elif 'mkldnn' in params.backend:
            raise ValueError("MKL-DNN is not supported yet.")
        elif 'openmp' in params.backend:
            torch.backends.openmp.enabled = True

    multidevice = False
    if "," in str(params.gpu):
        devices = params.gpu.split(',')
        multidevice = True

        if 'c' in str(devices[0]).lower():
            backward_device = "cpu"
            setup_cuda(), setup_cpu()
        else:
            backward_device = "cuda:" + devices[0]
            setup_cuda()
        dtype = torch.FloatTensor

    elif "c" not in str(params.gpu).lower():
        setup_cuda()
        dtype, backward_device = torch.cuda.FloatTensor, "cuda:" + str(params.gpu)
    else:
        setup_cpu()
        dtype, backward_device = torch.FloatTensor, "cpu"
    return dtype, multidevice, backward_device


def setup_multi_device(net):
    assert len(params.gpu.split(',')) - 1 == len(params.multidevice_strategy.split(',')), \
      "The number of -multidevice_strategy layer indices minus 1, must be equal to the number of -gpu devices."

    new_net = ModelParallel(net, params.gpu, params.multidevice_strategy)
    return new_net


# Preprocess an image before passing it to a model.
# We need to rescale from [0, 1] to [0, 255], convert from RGB to BGR,
# and subtract the mean pixel.
def preprocess(image_name, image_size):
    image = Image.open(image_name).convert('RGB')
    if type(image_size) is not tuple:
        image_size = tuple([int((float(image_size) / max(image.size))*x) for x in (image.height, image.width)])
    Loader = transforms.Compose([transforms.Resize(image_size), transforms.ToTensor()])
    rgb2bgr = transforms.Compose([transforms.Lambda(lambda x: x[torch.LongTensor([2,1,0])])])
    Normalize = transforms.Compose([transforms.Normalize(mean=[103.939, 116.779, 123.68], std=[1,1,1])])
    tensor = Normalize(rgb2bgr(Loader(image) * 255)).unsqueeze(0)
    return tensor


#  Undo the above preprocessing.
def deprocess(output_tensor):
    Normalize = transforms.Compose([transforms.Normalize(mean=[-103.939, -116.779, -123.68], std=[1,1,1])])
    bgr2rgb = transforms.Compose([transforms.Lambda(lambda x: x[torch.LongTensor([2,1,0])])])
    output_tensor = bgr2rgb(Normalize(output_tensor.squeeze(0).cpu())) / 255
    output_tensor.clamp_(0, 1)
    Image2PIL = transforms.ToPILImage()
    image = Image2PIL(output_tensor.cpu())
    return image


# Combine the Y channel of the generated image and the UV/CbCr channels of the
# content image to perform color-independent style transfer.
def original_colors(content, generated):
    content_channels = list(content.convert('YCbCr').split())
    generated_channels = list(generated.convert('YCbCr').split())
    content_channels[0] = generated_channels[0]
    return Image.merge('YCbCr', content_channels).convert('RGB')


# Print like Lua/Torch7
def print_torch(net, multidevice):
    if multidevice:
        return
    simplelist = ""
    for i, layer in enumerate(net, 1):
        simplelist = simplelist + "(" + str(i) + ") -> "
    print("nn.Sequential ( \n  [input -> " + simplelist + "output]")

    def strip(x):
        return str(x).replace(", ",',').replace("(",'').replace(")",'') + ", "
    def n():
        return "  (" + str(i) + "): " + "nn." + str(l).split("(", 1)[0]

    for i, l in enumerate(net, 1):
         if "2d" in str(l):
             ks, st, pd = strip(l.kernel_size), strip(l.stride), strip(l.padding)
             if "Conv2d" in str(l):
                 ch = str(l.in_channels) + " -> " + str(l.out_channels)
                 print(n() + "(" + ch + ", " + (ks).replace(",",'x', 1) + st + pd.replace(", ",')'))
             elif "Pool2d" in str(l):
                 st = st.replace("  ",' ') + st.replace(", ",')')
                 print(n() + "(" + ((ks).replace(",",'x' + ks, 1) + st).replace(", ",','))
         else:
             print(n())
    print(")")


# Divide weights by channel size
def normalize_weights(content_losses, style_losses):
    for n, i in enumerate(content_losses):
        i.strength = i.strength / max(i.target.size())
    for n, i in enumerate(style_losses):
        i.strength = i.strength / max(i.target.size())


# Scale gradients in the backward pass
class ScaleGradients(torch.autograd.Function):
    @staticmethod
    def forward(self, input_tensor, strength):
        self.strength = strength
        return input_tensor

    @staticmethod
    def backward(self, grad_output):
        grad_input = grad_output.clone()
        grad_input = grad_input / (torch.norm(grad_input, keepdim=True) + 1e-8)
        return grad_input * self.strength * self.strength, None


# Define an nn Module to compute content loss
class ContentLoss(nn.Module):

    def __init__(self, strength, normalize):
        super(ContentLoss, self).__init__()
        self.strength = strength
        self.crit = nn.MSELoss()
        self.mode = 'None'
        self.normalize = normalize

    def forward(self, input):
        if self.mode == 'loss':
            loss = self.crit(input, self.target)
            if self.normalize:
                loss = ScaleGradients.apply(loss, self.strength)
            self.loss = loss * self.strength
        elif self.mode == 'capture':
            self.target = input.detach()
        return input


class GramMatrix(nn.Module):

    def forward(self, input):
        B, C, H, W = input.size()
        x_flat = input.view(C, H * W)
        # Improvement 1
        # The Gram matrix of an image tensor (feature-wise outer product) using shifted activations
        return torch.mm(x_flat.add(-10), (x_flat.add(-10)).t())

# Improvement: Space Conversion Map Based Gram Matrix 
class ImprovedGramMatrixX(nn.Module):

    def forward(self, input):
        # B, C, H, W = input.size()
        # print(B, C, H, W)
        # dshift = input.index_fill(2, torch.tensor([0,1,2,3]).to('cuda:0'), 0)
        # ushift = input.index_fill(2, torch.tensor([H-1, H-2, H-3, H-4]).to('cuda:0'), 0)
        # rshift = input.index_fill(3, torch.tensor([0,1,2,3]).to('cuda:0'), 0)
        # lshift = input.index_fill(3, torch.tensor([W-1, W-2, W-3, W-4]).to('cuda:0'), 0)
        rshift = input[:,:,:,4:]
        lshift = input[:,:,:,:-4]
        B, C, H, W = rshift.size()
        # print(B, C, H, W)
        # x_flat = input.view(C, H * W)   # flatten

        l_flat = lshift.contiguous().view(C, H * W)
        r_flat = rshift.contiguous().view(C, H * W)
        # d_flat = dshift.view(C, H * W)
        # u_flat = ushift.view(C, H * W)

        # return torch.mm(x_flat.add(-1), (x_flat.add(-1)).t())
        return torch.mm(l_flat.add(-5), r_flat.add(-5).t())
        # return 0.5 * (torch.mm(l_flat.add(-1), (x_flat.add(-1)).t()) + torch.mm(r_flat.add(-1), (x_flat.add(-1)).t()))

class ImprovedGramMatrixY(nn.Module):

    def forward(self, input):
        # B, C, H, W = input.size()

        # dshift = input.index_fill(2, torch.tensor([0,1,2,3]).to('cuda:0'), 0)
        # ushift = input.index_fill(2, torch.tensor([H-1, H-2, H-3, H-4]).to('cuda:0'), 0)
        # lshift = input.index_fill(3, torch.tensor([0,1,2,3]), 0)
        # rshift = input.index_fill(3, torch.tensor([W-1, W-2, W-3, W-4]), 0)
        dshift = input[:,:,4:,:]
        ushift = input[:,:,:-4,:]
        B, C, H, W = ushift.size()

        # x_flat = input.view(C, H * W)   # flatten

        # l_flat = lshift.view(C, H * W)
        # r_flat = rshift.view(C, H * W)
        d_flat = dshift.contiguous().view(C, H * W)
        u_flat = ushift.contiguous().view(C, H * W)

        # return torch.mm(x_flat.add(-1), (x_flat.add(-1)).t())
        return torch.mm(u_flat.add(-5), d_flat.add(-5).t())
        # return 0.5 * (torch.mm(u_flat.add(-1), (x_flat.add(-1)).t()) + torch.mm(d_flat.add(-1), (x_flat.add(-1)).t()))

# Define an nn Module to compute style loss
class StyleLoss(nn.Module):

    def __init__(self, strength, normalize):
        super(StyleLoss, self).__init__()
        self.target = torch.Tensor()
        self.strength = strength
        self.gram = GramMatrix()

        # Improvement Test
        self.gramx = ImprovedGramMatrixX()
        self.gramy = ImprovedGramMatrixY()

        self.crit = nn.MSELoss()
        self.mode = 'None'
        self.blend_weight = None
        self.normalize = normalize

    def forward(self, input):
        # Improvement: New Loss Function
        if params.improve_gram:
            self.Gx = self.gramx(input)
            self.Gy = self.gramy(input)

            self.G = 0.5 * (self.Gx + self.Gy)
        else:
            self.G = self.gram(input)

        self.G = self.G.div(input.nelement())
        if self.mode == 'capture':
            if self.blend_weight == None:
                self.target = self.G.detach()
            elif self.target.nelement() == 0:
                self.target = self.G.detach().mul(self.blend_weight)
            else:
                self.target = self.target.add(self.blend_weight, self.G.detach())
        elif self.mode == 'loss':
            loss = self.crit(self.G, self.target)
            if self.normalize:
                loss = ScaleGradients.apply(loss, self.strength)
            self.loss = self.strength * loss
        return input


class TVLoss(nn.Module):

    def __init__(self, strength):
        super(TVLoss, self).__init__()
        self.strength = strength

    def forward(self, input):
        self.x_diff = input[:,:,1:,:] - input[:,:,:-1,:]
        self.y_diff = input[:,:,:,1:] - input[:,:,:,:-1]
        self.loss = self.strength * (torch.sum(torch.abs(self.x_diff)) + torch.sum(torch.abs(self.y_diff)))
        return input


if __name__ == "__main__":
    main()
