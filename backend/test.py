from preprocessing.utils.application import run as match
from preprocessing.core import Params
from postprocessing.color_transfer import color_trans

# param = {"match_proportion":"1","color_space": "rgb", "source_path":"latrobe.jpg", "reference_path":"rain-princess.jpg", "channels":"0,1,2", "result_path":"test.png", "verify_input":"False", "plot":"False"}
# match("fdm", Params(param))

color_trans("bird_muse_rgb_19_at_iteration_50.png", "bird.png", mask=0, hist_match=0)
# color_trans("xxx.png", "golden_gate.jpg", mask=0, hist_match=0)
