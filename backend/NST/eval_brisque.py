import torch
import piq
from skimage.io import imread

@torch.no_grad()
def main():
    x = (torch.tensor(imread('bird.png')).permute(2, 0, 1)[None, ...] / 255.).cuda()
    
    y1 = (torch.tensor(imread('testing_res/farmer/bird_farmer_wo.png')).permute(2, 0, 1)[None, ...] / 255.).cuda()
    y2 = (torch.tensor(imread('testing_res/farmer/bird_farmer.png')).permute(2, 0, 1)[None, ...] / 255.).cuda()
    y3 = (torch.tensor(imread('testing_res/farmer/fdm_lab_farmer.png')).permute(2, 0, 1)[None, ...] / 255.).cuda()
    

    # To compute BRISQUE score as a measure, use lower case function from the library
    content_brisque_index: torch.Tensor = piq.brisque(x, data_range=1., reduction='none')
    original_brisque_index = piq.brisque(y1, data_range=1., reduction='none')
    improved_brisque_index = piq.brisque(y2, data_range=1., reduction='none')
    color_brisque_index = piq.brisque(y3, data_range=1., reduction='none')
    # In order to use BRISQUE as a loss function, use corresponding PyTorch module.
    # Note: the back propagation is not available using torch==1.5.0.
    # Update the environment with latest torch and torchvision.
    # brisque_loss: torch.Tensor = piq.BRISQUELoss(data_range=1., reduction='none')(y)
    print(f"content BRISQUE score: {content_brisque_index.item():0.4f}")
    print(f"original BRISQUE score: {original_brisque_index.item():0.4f}")
    print(f"improved BRISQUE score: {improved_brisque_index.item():0.4f}")
    print(f"color BRISQUE score: {color_brisque_index.item():0.4f}")

if __name__ == '__main__':
    main()
