import argparse

import torch
from PIL import Image
from torchvision.transforms import ToTensor, ToPILImage

from .model import Generator

# parser = argparse.ArgumentParser(description='Test Single Image')
# parser.add_argument('--upscale_factor', default=2, type=int, help='super resolution upscale factor')
# parser.add_argument('--test_mode', default='GPU', type=str, choices=['GPU', 'CPU'], help='using GPU or CPU')
# parser.add_argument('--image_name', type=str, help='test low resolution image name')
# parser.add_argument('--model_name', default='netG_epoch_2_100.pth', type=str, help='generator model epoch name')
# opt = parser.parse_args()

# upscale_factor = opt.upscale_factor
# TEST_MODE = True if opt.test_mode == 'GPU' else False
# IMAGE_NAME = opt.image_name
# MODEL_NAME = opt.model_name

def sr_image(upscale_factor, image_path, use_cuda=True):
    model = Generator(upscale_factor).eval()
    if upscale_factor == 2:
        model_name = 'netG_epoch_2_100.pth'
    elif upscale_factor == 4:
        model_name = 'netG_epoch_4_100.pth'
    else:
        print('Wrong number: upscale_factor must be 2 or 4!')

    if use_cuda:
        model.cuda()
        model.load_state_dict(torch.load('srgan/epochs/' + model_name))
    else:
        model.load_state_dict(torch.load('srgan/epochs/' + model_name, map_location=lambda storage, loc: storage))

    image = Image.open(image_path)
    image = ToTensor()(image).unsqueeze(0)
    if use_cuda:
        image = image.cuda()

    # start = time.clock()
    out = model(image)
    # elapsed = (time.clock() - start)
    # print('cost' + str(elapsed) + 's')
    out_img = ToPILImage()(out[0].data.cpu())
    out_img.save('out_srf_' + str(upscale_factor) + '_' + image_path)
