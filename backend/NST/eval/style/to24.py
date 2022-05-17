import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import os
import sys
import shutil


f = 'escher_sphere.jpg'

img=Image.open(f).convert('RGB')
dirpath = 'escher_sphere_24.jpg'
file_name, file_extend = os.path.splitext(f)
# dst = os.path.join(os.path.abspath(dirpath), file_name + '.jpg')
img.save(dirpath)
