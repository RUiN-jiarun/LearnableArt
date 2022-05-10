STYLE_IMAGE1=input/farmer.png
CONTENT_IMAGE1_1=input/hm_rgb.png
CONTENT_IMAGE1_2=input/hm_lab.png
CONTENT_IMAGE1_3=input/fdm_rgb.png
CONTENT_IMAGE1_4=input/fdm_hsv.png
CONTENT_IMAGE1_5=input/fdm_lab.png
CONTENT_IMAGE1_6=input/bird.png

PYTHON=python3 # Change to Python if using Python 2
SCRIPT=neural_style.py

NEURAL_STYLE=$PYTHON
NEURAL_STYLE+=" "
NEURAL_STYLE+=$SCRIPT

$NEURAL_STYLE \
  -content_image $CONTENT_IMAGE1_1 \
  -style_image $STYLE_IMAGE1 \
  -output_image res/hm_rgb_farmer.png \
  -backend cudnn -cudnn_autotune -improve_gram

$NEURAL_STYLE \
  -content_image $CONTENT_IMAGE1_2 \
  -style_image $STYLE_IMAGE1 \
  -output_image res/hm_lab_farmer.png \
  -backend cudnn -cudnn_autotune -improve_gram
  
$NEURAL_STYLE \
  -content_image $CONTENT_IMAGE1_3 \
  -style_image $STYLE_IMAGE1 \
  -output_image res/fdm_rgb_farmer.png \
  -backend cudnn -cudnn_autotune -improve_gram
  
$NEURAL_STYLE \
  -content_image $CONTENT_IMAGE1_4 \
  -style_image $STYLE_IMAGE1 \
  -output_image res/fdm_hsv_farmer.png \
  -backend cudnn -cudnn_autotune -improve_gram
  
$NEURAL_STYLE \
  -content_image $CONTENT_IMAGE1_5 \
  -style_image $STYLE_IMAGE1 \
  -output_image res/fdm_lab_farmer.png \
  -backend cudnn -cudnn_autotune -improve_gram
  
$NEURAL_STYLE \
  -content_image $CONTENT_IMAGE1_6 \
  -style_image $STYLE_IMAGE1 \
  -output_image res/farmer.png \
  -backend cudnn -cudnn_autotune -improve_gram
