STYLE_IMAGE1=input/la_muse.jpg
CONTENT_IMAGE1_1=input/hm_rgb_brad_muse.png
CONTENT_IMAGE1_2=input/hm_lab_brad_muse.png
CONTENT_IMAGE1_3=input/fdm_rgb_brad_muse.png
CONTENT_IMAGE1_4=input/fdm_hsv_brad_muse.png
CONTENT_IMAGE1_5=input/fdm_lab_brad_muse.png
CONTENT_IMAGE1_6=input/brad_pitt.jpg
STYLE_IMAGE2=input/hbh.jpg
CONTENT_IMAGE2_1=input/hm_rgb_hbh.png
CONTENT_IMAGE2_2=input/hm_lab_hbh.png
CONTENT_IMAGE2_3=input/fdm_rgb_hbh.png
CONTENT_IMAGE2_4=input/fdm_hsv_hbh.png
CONTENT_IMAGE2_5=input/fdm_lab_hbh.png
CONTENT_IMAGE2_6=input/waterfall.jpg
STYLE_IMAGE3=input/shitao.jpg
CONTENT_IMAGE3_1=input/hm_rgb_st.png
CONTENT_IMAGE3_2=input/hm_lab_st.png
CONTENT_IMAGE3_3=input/fdm_rgb_st.png
CONTENT_IMAGE3_4=input/fdm_hsv_st.png
CONTENT_IMAGE3_5=input/fdm_lab_st.png
CONTENT_IMAGE3_6=input/waterfall.jpg
STYLE_IMAGE4=input/rain-princess.jpg
CONTENT_IMAGE4_1=input/hm_rgb_rain.png
CONTENT_IMAGE4_2=input/hm_lab_rain.png
CONTENT_IMAGE4_3=input/fdm_rgb_rain.png
CONTENT_IMAGE4_4=input/fdm_hsv_rain.png
CONTENT_IMAGE4_5=input/fdm_lab_rain.png
CONTENT_IMAGE4_6=input/bird.png

PYTHON=python3 # Change to Python if using Python 2
SCRIPT=neural_style.py

NEURAL_STYLE=$PYTHON
NEURAL_STYLE+=" "
NEURAL_STYLE+=$SCRIPT

$NEURAL_STYLE \
  -content_image $CONTENT_IMAGE1_1 \
  -style_image $STYLE_IMAGE1 \
  -output_image res/hm_rgb_brad_muse.png \
  -backend cudnn -cudnn_autotune -improve_gram

$NEURAL_STYLE \
  -content_image $CONTENT_IMAGE1_2 \
  -style_image $STYLE_IMAGE1 \
  -output_image res/hm_lab_brad_muse.png \
  -backend cudnn -cudnn_autotune -improve_gram
  
$NEURAL_STYLE \
  -content_image $CONTENT_IMAGE1_3 \
  -style_image $STYLE_IMAGE1 \
  -output_image res/fdm_rgb_brad_muse.png \
  -backend cudnn -cudnn_autotune -improve_gram
  
$NEURAL_STYLE \
  -content_image $CONTENT_IMAGE1_4 \
  -style_image $STYLE_IMAGE1 \
  -output_image res/fdm_hsv_brad_muse.png \
  -backend cudnn -cudnn_autotune -improve_gram
  
$NEURAL_STYLE \
  -content_image $CONTENT_IMAGE1_5 \
  -style_image $STYLE_IMAGE1 \
  -output_image res/fdm_lab_brad_muse.png \
  -backend cudnn -cudnn_autotune -improve_gram
  
$NEURAL_STYLE \
  -content_image $CONTENT_IMAGE1_6 \
  -style_image $STYLE_IMAGE1 \
  -output_image res/brad_muse.png \
  -backend cudnn -cudnn_autotune -improve_gram

$NEURAL_STYLE \
  -content_image $CONTENT_IMAGE2_1 \
  -style_image $STYLE_IMAGE2 \
  -output_image res/hm_rgb_hbh.png \
  -backend cudnn -cudnn_autotune -improve_gram

$NEURAL_STYLE \
  -content_image $CONTENT_IMAGE2_2 \
  -style_image $STYLE_IMAGE2 \
  -output_image res/hm_lab_hbh.png \
  -backend cudnn -cudnn_autotune -improve_gram
  
$NEURAL_STYLE \
  -content_image $CONTENT_IMAGE2_3 \
  -style_image $STYLE_IMAGE2 \
  -output_image res/fdm_rgb_hbh.png \
  -backend cudnn -cudnn_autotune -improve_gram
  
$NEURAL_STYLE \
  -content_image $CONTENT_IMAGE2_4 \
  -style_image $STYLE_IMAGE2 \
  -output_image res/fdm_hsv_hbh.png \
  -backend cudnn -cudnn_autotune -improve_gram
  
$NEURAL_STYLE \
  -content_image $CONTENT_IMAGE2_5 \
  -style_image $STYLE_IMAGE2 \
  -output_image res/fdm_lab_hbh.png \
  -backend cudnn -cudnn_autotune -improve_gram
  
$NEURAL_STYLE \
  -content_image $CONTENT_IMAGE2_6 \
  -style_image $STYLE_IMAGE2 \
  -output_image res/waterfall_hbh.png \
  -backend cudnn -cudnn_autotune -improve_gram

$NEURAL_STYLE \
  -content_image $CONTENT_IMAGE3_1 \
  -style_image $STYLE_IMAGE3 \
  -output_image res/hm_rgb_st.png \
  -backend cudnn -cudnn_autotune -improve_gram

$NEURAL_STYLE \
  -content_image $CONTENT_IMAGE3_2 \
  -style_image $STYLE_IMAGE3 \
  -output_image res/hm_lab_st.png \
  -backend cudnn -cudnn_autotune -improve_gram
  
$NEURAL_STYLE \
  -content_image $CONTENT_IMAGE3_3 \
  -style_image $STYLE_IMAGE3 \
  -output_image res/fdm_rgb_st.png \
  -backend cudnn -cudnn_autotune -improve_gram
  
$NEURAL_STYLE \
  -content_image $CONTENT_IMAGE3_4 \
  -style_image $STYLE_IMAGE3 \
  -output_image res/fdm_hsv_st.png \
  -backend cudnn -cudnn_autotune -improve_gram
  
$NEURAL_STYLE \
  -content_image $CONTENT_IMAGE3_5 \
  -style_image $STYLE_IMAGE3 \
  -output_image res/fdm_lab_st.png \
  -backend cudnn -cudnn_autotune -improve_gram
  
$NEURAL_STYLE \
  -content_image $CONTENT_IMAGE3_6 \
  -style_image $STYLE_IMAGE3 \
  -output_image res/waterfall_st.png \
  -backend cudnn -cudnn_autotune -improve_gram

$NEURAL_STYLE \
  -content_image $CONTENT_IMAGE4_1 \
  -style_image $STYLE_IMAGE4 \
  -output_image res/hm_rgb_rain.png \
  -backend cudnn -cudnn_autotune -improve_gram

$NEURAL_STYLE \
  -content_image $CONTENT_IMAGE4_2 \
  -style_image $STYLE_IMAGE4 \
  -output_image res/hm_lab_rain.png \
  -backend cudnn -cudnn_autotune -improve_gram
  
$NEURAL_STYLE \
  -content_image $CONTENT_IMAGE4_3 \
  -style_image $STYLE_IMAGE4 \
  -output_image res/fdm_rgb_rain.png \
  -backend cudnn -cudnn_autotune -improve_gram
  
$NEURAL_STYLE \
  -content_image $CONTENT_IMAGE4_4 \
  -style_image $STYLE_IMAGE4 \
  -output_image res/fdm_hsv_rain.png \
  -backend cudnn -cudnn_autotune -improve_gram
  
$NEURAL_STYLE \
  -content_image $CONTENT_IMAGE4_5 \
  -style_image $STYLE_IMAGE4 \
  -output_image res/fdm_lab_rain.png \
  -backend cudnn -cudnn_autotune -improve_gram
  
$NEURAL_STYLE \
  -content_image $CONTENT_IMAGE4_6 \
  -style_image $STYLE_IMAGE4 \
  -output_image res/bird_rain.png \
  -backend cudnn -cudnn_autotune -improve_gram