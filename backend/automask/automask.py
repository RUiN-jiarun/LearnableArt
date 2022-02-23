import u2net.mask
import numpy as np
import io
from PIL import Image, ImageFile
import argparse
import time
import os

parser = argparse.ArgumentParser(description='Auto mask generator')
parser.add_argument('input_path', type=str, 
                    help='Path to the image to masked.')

parser.add_argument('--bg', default='False', type=str,
                    help="'True' to preserve background, 'False' to preserve foreground.")

parser.add_argument('--dilate', default=1, type=int,
                    help="Convolution core size of dilating. Make sure is an odd number!")

parser.add_argument('--model', default='u2netp', type=str,
                    help="Choices are 'u2net', 'u2netp' and 'u2net_human_seg'.")

def str_to_bool(v):
    return v.lower() in ("true", "yes", "t", "1")

args = parser.parse_args()
input_path = args.input_path
# input_path = 'Latte.jpg'
# output_path = 'out2.png'
output_path = os.path.splitext(input_path)[0] + "_mask.png"
isBackground = str_to_bool(args.bg)
model_name = args.model
dilate_structure_size = args.dilate



def automask(input_path : str, bg=False, dilate=1, model='u2netp'):
    output_path = os.path.splitext(input_path)[0] + "_mask.png"
    # Uncomment the following line if working with trucated image formats (ex. JPEG / JPG)
    if input_path.endswith('.jpg'):
        ImageFile.LOAD_TRUNCATED_IMAGES = True

    f = np.fromfile(input_path)

    start = time.time()
    result = u2net.mask.generate(f, model_name=model, isBackground=bg, dilate_structure_size=dilate)
    end = time.time()
    print('Running time: %s seconds' %(end - start))

    img = Image.open(io.BytesIO(result)).convert("RGBA")
    img.save(output_path)