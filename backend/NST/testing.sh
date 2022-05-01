STYLE_IMAGE=input/the_scream.jpg
CONTENT_IMAGE1=input/hm_rgb_tubingen.png
CONTENT_IMAGE2=input/hm_lab_tubingen.png
CONTENT_IMAGE3=input/fdm_rgb_tubingen.png
CONTENT_IMAGE4=input/fdm_hsv_tubingen.png
CONTENT_IMAGE5=input/fdm_lab_tubingen.png
CONTENT_IMAGE6=input/tubingen.jpg

PYTHON=python3 # Change to Python if using Python 2
SCRIPT=neural_style.py

NEURAL_STYLE=$PYTHON
NEURAL_STYLE+=" "
NEURAL_STYLE+=$SCRIPT

$NEURAL_STYLE \
  -content_image $CONTENT_IMAGE1 \
  -style_image $STYLE_IMAGE \
  -output_image hm_rgb_tubingen_scream.png \
  -backend cudnn -cudnn_autotune -improve_gram

$NEURAL_STYLE \
  -content_image $CONTENT_IMAGE2 \
  -style_image $STYLE_IMAGE \
  -output_image hm_lab_tubingen_scream.png \
  -backend cudnn -cudnn_autotune -improve_gram
  
$NEURAL_STYLE \
  -content_image $CONTENT_IMAGE3 \
  -style_image $STYLE_IMAGE \
  -output_image fdm_rgb_tubingen_scream.png \
  -backend cudnn -cudnn_autotune -improve_gram
  
$NEURAL_STYLE \
  -content_image $CONTENT_IMAGE4 \
  -style_image $STYLE_IMAGE \
  -output_image fdm_hsv_tubingen_scream.png \
  -backend cudnn -cudnn_autotune -improve_gram
  
$NEURAL_STYLE \
  -content_image $CONTENT_IMAGE5 \
  -style_image $STYLE_IMAGE \
  -output_image fdm_lab_tubingen_scream.png \
  -backend cudnn -cudnn_autotune -improve_gram
  
$NEURAL_STYLE \
  -content_image $CONTENT_IMAGE6 \
  -style_image $STYLE_IMAGE \
  -output_image tubingen_scream.png \
  -backend cudnn -cudnn_autotune -improve_gram