# from preprocessing.utils.application import run as match
# from preprocessing.core import Params
# from postprocessing.color_transfer import color_trans
# from NST.neural_style_jt import param_main
# from NST.neural_style import param_main
from postprocessing.mask_transfer import mask_trans
from srgan.sr import sr_image
from postprocessing.palette_transfer import palette_trans

# param = {"match_proportion":"1","color_space": "rgb", "source_path":"latrobe.jpg", "reference_path":"rain-princess.jpg", "channels":"0,1,2", "result_path":"test.png", "verify_input":"False", "plot":"False"}
# match("fdm", Params(param))

# color_trans("bird_muse_rgb_19_at_iteration_50.png", "bird.png", mask=0, hist_match=0)
# color_trans("xxx.png", "golden_gate.jpg", mask=0, hist_match=0)

# param_main("bird.png", "rain-princess.jpg", "output.png")
# mask_trans("output_400.png", "bird.png", "birdmask.png")
# print(bool(int('0')))
# sr_image(2, 'output_400.png', 'test.jpg')
# f = float('5e-2')
# print(f)
# print(type(f))
palette_trans('output_400.png', 'palette_test_green.png', 150)
