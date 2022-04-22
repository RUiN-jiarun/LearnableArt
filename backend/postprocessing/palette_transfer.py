import colorsys
from PIL import Image

def palette_trans(input_path, output_path, target_h):

    image = Image.open(input_path).convert('RGBA')

    image.load()
    r, g, b, a = image.split()
    result_r, result_g, result_b, result_a = [], [], [], []

    for pixel_r, pixel_g, pixel_b, pixel_a in zip(r.getdata(), g.getdata(), b.getdata(), a.getdata()):
        h, s, v = colorsys.rgb_to_hsv(pixel_r / 255., pixel_b / 255., pixel_g / 255.)
        # print(h,s,v)
        rgb = colorsys.hsv_to_rgb(target_h / 355., s, v)
        pixel_r, pixel_g, pixel_b = [int(x * 255.) for x in rgb]
        result_r.append(pixel_r)
        result_g.append(pixel_g)
        result_b.append(pixel_b)
        result_a.append(pixel_a)

    r.putdata(result_r)
    g.putdata(result_g)
    b.putdata(result_b)
    a.putdata(result_a)

    image = Image.merge('RGBA', (r, g, b, a))

    image.save(output_path)