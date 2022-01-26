import functools
import io

import numpy as np
from PIL import Image
import PIL.ImageOps
import PIL.ImageFilter
from pymatting.alpha.estimate_alpha_cf import estimate_alpha_cf
from pymatting.foreground.estimate_foreground_ml import estimate_foreground_ml
from pymatting.util.util import stack_images
from scipy.ndimage.morphology import binary_erosion

from .detect import load_model, predict


def naive_cutout(img, mask):
    black = Image.new("RGBA", (img.size), (0,0,0,255))
    empty = Image.new("RGBA", (img.size), (255,255,255,255))
    cutout = Image.composite(empty, black, mask.resize(img.size, Image.LANCZOS))
    return cutout


@functools.lru_cache(maxsize=None)
def get_model(model_name):
    if model_name == "u2netp":
        return load_model(model_name="u2netp")
    if model_name == "u2net_human_seg":
        return load_model(model_name="u2net_human_seg")
    else:
        return load_model(model_name="u2net")


def resize_image(img, width, height):
    original_width, original_height = img.size
    width = original_width if width is None else width
    height = original_height if height is None else height
    return (
        img.resize((width, height))
        if original_width != width or original_height != height
        else img
    )


def generate(
    data,
    model_name="u2netp",
    isBackground=False,
    dilate_structure_size=1,
    width=None,
    height=None,
):
    img = Image.open(io.BytesIO(data)).convert("RGB")
    if width is not None or height is not None:
        img = resize_image(img, width, height)

    model = get_model(model_name)
    mask = predict(model, np.array(img)).convert("L")

    
    cutout = naive_cutout(img, mask)

    if isBackground:
        if cutout.mode == 'RGBA':
            r, g, b, a = cutout.split()
            rgb_img = Image.merge('RGB', (r, g, b))
            inverted_img = PIL.ImageOps.invert(rgb_img)
            _r, _g, _b = inverted_img.split()
            cutout = Image.merge('RGBA', (_r, _g, _b, a))
        else:
            cutout = PIL.ImageOps.invert(cutout)

    bio = io.BytesIO()
    cutout.convert('1')
    # erode
    cutout = cutout.filter(PIL.ImageFilter.MinFilter(dilate_structure_size))
    cutout.save(bio, "PNG")

    return bio.getbuffer()
