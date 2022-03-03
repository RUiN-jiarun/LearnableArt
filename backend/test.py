from preprocessing.utils.application import run as match
from preprocessing.core import Params

param = {"match_proportion":"1","color_space": "rgb", "source_path":"latrobe.jpg", "reference_path":"rain-princess.jpg", "channels":"0,1,2", "result_path":"test.png", "verify_input":"False", "plot":"False"}
match("fdm", Params(param))

