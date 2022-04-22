import torch
import piq
from skimage.io import imread

@torch.no_grad()
def main():
    y = (torch.tensor(imread('out.png')).permute(2, 0, 1)[None, ...] / 255.).cuda()
    x = (torch.tensor(imread('out_800.png')).permute(2, 0, 1)[None, ...] / 255.).cuda()

    # To compute MS-SSIM index as a measure, use lower case function from the library:
    ms_ssim_index: torch.Tensor = piq.multi_scale_ssim(x, y, data_range=1.)
    # In order to use MS-SSIM as a loss function, use corresponding PyTorch module:
    ms_ssim_loss = piq.MultiScaleSSIMLoss(data_range=1., reduction='none')(x, y)
    print(f"MS-SSIM index: {ms_ssim_index.item():0.4f}, loss: {ms_ssim_loss.item():0.4f}")

    # To compute PSNR as a measure, use lower case function from the library.
    psnr_index = piq.psnr(x, y, data_range=1., reduction='none')
    print(f"PSNR index: {psnr_index.item():0.4f}")

    # To compute SSIM index as a measure, use lower case function from the library:
    ssim_index = piq.ssim(x, y, data_range=1.)
    # In order to use SSIM as a loss function, use corresponding PyTorch module:
    ssim_loss: torch.Tensor = piq.SSIMLoss(data_range=1.)(x, y)
    print(f"SSIM index: {ssim_index.item():0.4f}, loss: {ssim_loss.item():0.4f}")

if __name__ == '__main__':
    main()

