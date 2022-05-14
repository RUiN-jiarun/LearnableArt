CONTENT_1=content/2B_eye.jpg
CONTENT_2=content/2B_head.jpg
CONTENT_3=content/Aurea-Luna.jpg
CONTENT_4=content/bird.png
CONTENT_5=content/brad_pitt.jpg
CONTENT_6=content/chicago.jpg
CONTENT_7=content/golden_gate.jpg
CONTENT_8=content/hoovertowernight.jpg
CONTENT_9=content/horse.jpg
CONTENT_10=content/leonardo.jpg
CONTENT_11=content/lotus.jpg
CONTENT_12=content/mill.jpg
CONTENT_13=content/singer.jpg
CONTENT_14=content/stata.jpg
CONTENT_15=content/sunset.jpg
CONTENT_16=content/tubingen.jpg
CONTENT_17=content/waterfall.jpg
STYLE_1=style/candy-style.jpg
STYLE_2=style/escher_sphere.jpg
STYLE_3=style/face.jpg
STYLE_4=style/farmer_paint.png
STYLE_5=style/golden.jpg
STYLE_6=style/hbh.jpg
STYLE_7=style/la_muse.jpg
STYLE_8=style/matisse.jpg
STYLE_9=style/monet.jpg
STYLE_10=style/persia_horse.jpg
STYLE_11=style/rain-princess.jpg
STYLE_12=style/seated-nude.jpg
STYLE_13=style/starry_night.jpg
STYLE_14=style/style2.jpg
STYLE_15=style/the_scream.jpg
PYTHON=python3
SCRIPT=neural_style.py
NEURAL_STYLE=$PYTHON
NEURAL_STYLE+=" "
NEURAL_STYLE+=$SCRIPT
$NEURAL_STYLE \
  -content_image $CONTENT_1 \
  -style_image $STYLE_1 \
  -output_image ori/1_1.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_1 \
  -style_image $STYLE_2 \
  -output_image ori/1_2.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_1 \
  -style_image $STYLE_3 \
  -output_image ori/1_3.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_1 \
  -style_image $STYLE_4 \
  -output_image ori/1_4.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_1 \
  -style_image $STYLE_5 \
  -output_image ori/1_5.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_1 \
  -style_image $STYLE_6 \
  -output_image ori/1_6.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_1 \
  -style_image $STYLE_7 \
  -output_image ori/1_7.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_1 \
  -style_image $STYLE_8 \
  -output_image ori/1_8.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_1 \
  -style_image $STYLE_9 \
  -output_image ori/1_9.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_1 \
  -style_image $STYLE_10 \
  -output_image ori/1_10.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_1 \
  -style_image $STYLE_11 \
  -output_image ori/1_11.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_1 \
  -style_image $STYLE_12 \
  -output_image ori/1_12.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_1 \
  -style_image $STYLE_13 \
  -output_image ori/1_13.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_1 \
  -style_image $STYLE_14 \
  -output_image ori/1_14.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_1 \
  -style_image $STYLE_15 \
  -output_image ori/1_15.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_2 \
  -style_image $STYLE_1 \
  -output_image ori/2_1.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_2 \
  -style_image $STYLE_2 \
  -output_image ori/2_2.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_2 \
  -style_image $STYLE_3 \
  -output_image ori/2_3.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_2 \
  -style_image $STYLE_4 \
  -output_image ori/2_4.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_2 \
  -style_image $STYLE_5 \
  -output_image ori/2_5.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_2 \
  -style_image $STYLE_6 \
  -output_image ori/2_6.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_2 \
  -style_image $STYLE_7 \
  -output_image ori/2_7.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_2 \
  -style_image $STYLE_8 \
  -output_image ori/2_8.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_2 \
  -style_image $STYLE_9 \
  -output_image ori/2_9.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_2 \
  -style_image $STYLE_10 \
  -output_image ori/2_10.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_2 \
  -style_image $STYLE_11 \
  -output_image ori/2_11.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_2 \
  -style_image $STYLE_12 \
  -output_image ori/2_12.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_2 \
  -style_image $STYLE_13 \
  -output_image ori/2_13.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_2 \
  -style_image $STYLE_14 \
  -output_image ori/2_14.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_2 \
  -style_image $STYLE_15 \
  -output_image ori/2_15.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_3 \
  -style_image $STYLE_1 \
  -output_image ori/3_1.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_3 \
  -style_image $STYLE_2 \
  -output_image ori/3_2.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_3 \
  -style_image $STYLE_3 \
  -output_image ori/3_3.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_3 \
  -style_image $STYLE_4 \
  -output_image ori/3_4.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_3 \
  -style_image $STYLE_5 \
  -output_image ori/3_5.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_3 \
  -style_image $STYLE_6 \
  -output_image ori/3_6.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_3 \
  -style_image $STYLE_7 \
  -output_image ori/3_7.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_3 \
  -style_image $STYLE_8 \
  -output_image ori/3_8.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_3 \
  -style_image $STYLE_9 \
  -output_image ori/3_9.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_3 \
  -style_image $STYLE_10 \
  -output_image ori/3_10.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_3 \
  -style_image $STYLE_11 \
  -output_image ori/3_11.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_3 \
  -style_image $STYLE_12 \
  -output_image ori/3_12.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_3 \
  -style_image $STYLE_13 \
  -output_image ori/3_13.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_3 \
  -style_image $STYLE_14 \
  -output_image ori/3_14.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_3 \
  -style_image $STYLE_15 \
  -output_image ori/3_15.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_4 \
  -style_image $STYLE_1 \
  -output_image ori/4_1.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_4 \
  -style_image $STYLE_2 \
  -output_image ori/4_2.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_4 \
  -style_image $STYLE_3 \
  -output_image ori/4_3.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_4 \
  -style_image $STYLE_4 \
  -output_image ori/4_4.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_4 \
  -style_image $STYLE_5 \
  -output_image ori/4_5.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_4 \
  -style_image $STYLE_6 \
  -output_image ori/4_6.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_4 \
  -style_image $STYLE_7 \
  -output_image ori/4_7.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_4 \
  -style_image $STYLE_8 \
  -output_image ori/4_8.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_4 \
  -style_image $STYLE_9 \
  -output_image ori/4_9.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_4 \
  -style_image $STYLE_10 \
  -output_image ori/4_10.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_4 \
  -style_image $STYLE_11 \
  -output_image ori/4_11.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_4 \
  -style_image $STYLE_12 \
  -output_image ori/4_12.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_4 \
  -style_image $STYLE_13 \
  -output_image ori/4_13.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_4 \
  -style_image $STYLE_14 \
  -output_image ori/4_14.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_4 \
  -style_image $STYLE_15 \
  -output_image ori/4_15.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_5 \
  -style_image $STYLE_1 \
  -output_image ori/5_1.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_5 \
  -style_image $STYLE_2 \
  -output_image ori/5_2.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_5 \
  -style_image $STYLE_3 \
  -output_image ori/5_3.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_5 \
  -style_image $STYLE_4 \
  -output_image ori/5_4.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_5 \
  -style_image $STYLE_5 \
  -output_image ori/5_5.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_5 \
  -style_image $STYLE_6 \
  -output_image ori/5_6.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_5 \
  -style_image $STYLE_7 \
  -output_image ori/5_7.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_5 \
  -style_image $STYLE_8 \
  -output_image ori/5_8.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_5 \
  -style_image $STYLE_9 \
  -output_image ori/5_9.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_5 \
  -style_image $STYLE_10 \
  -output_image ori/5_10.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_5 \
  -style_image $STYLE_11 \
  -output_image ori/5_11.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_5 \
  -style_image $STYLE_12 \
  -output_image ori/5_12.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_5 \
  -style_image $STYLE_13 \
  -output_image ori/5_13.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_5 \
  -style_image $STYLE_14 \
  -output_image ori/5_14.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_5 \
  -style_image $STYLE_15 \
  -output_image ori/5_15.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_6 \
  -style_image $STYLE_1 \
  -output_image ori/6_1.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_6 \
  -style_image $STYLE_2 \
  -output_image ori/6_2.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_6 \
  -style_image $STYLE_3 \
  -output_image ori/6_3.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_6 \
  -style_image $STYLE_4 \
  -output_image ori/6_4.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_6 \
  -style_image $STYLE_5 \
  -output_image ori/6_5.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_6 \
  -style_image $STYLE_6 \
  -output_image ori/6_6.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_6 \
  -style_image $STYLE_7 \
  -output_image ori/6_7.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_6 \
  -style_image $STYLE_8 \
  -output_image ori/6_8.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_6 \
  -style_image $STYLE_9 \
  -output_image ori/6_9.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_6 \
  -style_image $STYLE_10 \
  -output_image ori/6_10.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_6 \
  -style_image $STYLE_11 \
  -output_image ori/6_11.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_6 \
  -style_image $STYLE_12 \
  -output_image ori/6_12.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_6 \
  -style_image $STYLE_13 \
  -output_image ori/6_13.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_6 \
  -style_image $STYLE_14 \
  -output_image ori/6_14.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_6 \
  -style_image $STYLE_15 \
  -output_image ori/6_15.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_7 \
  -style_image $STYLE_1 \
  -output_image ori/7_1.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_7 \
  -style_image $STYLE_2 \
  -output_image ori/7_2.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_7 \
  -style_image $STYLE_3 \
  -output_image ori/7_3.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_7 \
  -style_image $STYLE_4 \
  -output_image ori/7_4.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_7 \
  -style_image $STYLE_5 \
  -output_image ori/7_5.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_7 \
  -style_image $STYLE_6 \
  -output_image ori/7_6.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_7 \
  -style_image $STYLE_7 \
  -output_image ori/7_7.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_7 \
  -style_image $STYLE_8 \
  -output_image ori/7_8.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_7 \
  -style_image $STYLE_9 \
  -output_image ori/7_9.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_7 \
  -style_image $STYLE_10 \
  -output_image ori/7_10.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_7 \
  -style_image $STYLE_11 \
  -output_image ori/7_11.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_7 \
  -style_image $STYLE_12 \
  -output_image ori/7_12.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_7 \
  -style_image $STYLE_13 \
  -output_image ori/7_13.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_7 \
  -style_image $STYLE_14 \
  -output_image ori/7_14.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_7 \
  -style_image $STYLE_15 \
  -output_image ori/7_15.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_8 \
  -style_image $STYLE_1 \
  -output_image ori/8_1.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_8 \
  -style_image $STYLE_2 \
  -output_image ori/8_2.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_8 \
  -style_image $STYLE_3 \
  -output_image ori/8_3.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_8 \
  -style_image $STYLE_4 \
  -output_image ori/8_4.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_8 \
  -style_image $STYLE_5 \
  -output_image ori/8_5.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_8 \
  -style_image $STYLE_6 \
  -output_image ori/8_6.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_8 \
  -style_image $STYLE_7 \
  -output_image ori/8_7.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_8 \
  -style_image $STYLE_8 \
  -output_image ori/8_8.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_8 \
  -style_image $STYLE_9 \
  -output_image ori/8_9.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_8 \
  -style_image $STYLE_10 \
  -output_image ori/8_10.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_8 \
  -style_image $STYLE_11 \
  -output_image ori/8_11.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_8 \
  -style_image $STYLE_12 \
  -output_image ori/8_12.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_8 \
  -style_image $STYLE_13 \
  -output_image ori/8_13.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_8 \
  -style_image $STYLE_14 \
  -output_image ori/8_14.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_8 \
  -style_image $STYLE_15 \
  -output_image ori/8_15.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_9 \
  -style_image $STYLE_1 \
  -output_image ori/9_1.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_9 \
  -style_image $STYLE_2 \
  -output_image ori/9_2.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_9 \
  -style_image $STYLE_3 \
  -output_image ori/9_3.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_9 \
  -style_image $STYLE_4 \
  -output_image ori/9_4.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_9 \
  -style_image $STYLE_5 \
  -output_image ori/9_5.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_9 \
  -style_image $STYLE_6 \
  -output_image ori/9_6.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_9 \
  -style_image $STYLE_7 \
  -output_image ori/9_7.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_9 \
  -style_image $STYLE_8 \
  -output_image ori/9_8.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_9 \
  -style_image $STYLE_9 \
  -output_image ori/9_9.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_9 \
  -style_image $STYLE_10 \
  -output_image ori/9_10.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_9 \
  -style_image $STYLE_11 \
  -output_image ori/9_11.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_9 \
  -style_image $STYLE_12 \
  -output_image ori/9_12.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_9 \
  -style_image $STYLE_13 \
  -output_image ori/9_13.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_9 \
  -style_image $STYLE_14 \
  -output_image ori/9_14.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_9 \
  -style_image $STYLE_15 \
  -output_image ori/9_15.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_10 \
  -style_image $STYLE_1 \
  -output_image ori/10_1.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_10 \
  -style_image $STYLE_2 \
  -output_image ori/10_2.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_10 \
  -style_image $STYLE_3 \
  -output_image ori/10_3.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_10 \
  -style_image $STYLE_4 \
  -output_image ori/10_4.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_10 \
  -style_image $STYLE_5 \
  -output_image ori/10_5.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_10 \
  -style_image $STYLE_6 \
  -output_image ori/10_6.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_10 \
  -style_image $STYLE_7 \
  -output_image ori/10_7.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_10 \
  -style_image $STYLE_8 \
  -output_image ori/10_8.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_10 \
  -style_image $STYLE_9 \
  -output_image ori/10_9.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_10 \
  -style_image $STYLE_10 \
  -output_image ori/10_10.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_10 \
  -style_image $STYLE_11 \
  -output_image ori/10_11.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_10 \
  -style_image $STYLE_12 \
  -output_image ori/10_12.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_10 \
  -style_image $STYLE_13 \
  -output_image ori/10_13.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_10 \
  -style_image $STYLE_14 \
  -output_image ori/10_14.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_10 \
  -style_image $STYLE_15 \
  -output_image ori/10_15.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_11 \
  -style_image $STYLE_1 \
  -output_image ori/11_1.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_11 \
  -style_image $STYLE_2 \
  -output_image ori/11_2.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_11 \
  -style_image $STYLE_3 \
  -output_image ori/11_3.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_11 \
  -style_image $STYLE_4 \
  -output_image ori/11_4.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_11 \
  -style_image $STYLE_5 \
  -output_image ori/11_5.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_11 \
  -style_image $STYLE_6 \
  -output_image ori/11_6.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_11 \
  -style_image $STYLE_7 \
  -output_image ori/11_7.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_11 \
  -style_image $STYLE_8 \
  -output_image ori/11_8.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_11 \
  -style_image $STYLE_9 \
  -output_image ori/11_9.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_11 \
  -style_image $STYLE_10 \
  -output_image ori/11_10.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_11 \
  -style_image $STYLE_11 \
  -output_image ori/11_11.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_11 \
  -style_image $STYLE_12 \
  -output_image ori/11_12.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_11 \
  -style_image $STYLE_13 \
  -output_image ori/11_13.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_11 \
  -style_image $STYLE_14 \
  -output_image ori/11_14.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_11 \
  -style_image $STYLE_15 \
  -output_image ori/11_15.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_12 \
  -style_image $STYLE_1 \
  -output_image ori/12_1.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_12 \
  -style_image $STYLE_2 \
  -output_image ori/12_2.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_12 \
  -style_image $STYLE_3 \
  -output_image ori/12_3.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_12 \
  -style_image $STYLE_4 \
  -output_image ori/12_4.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_12 \
  -style_image $STYLE_5 \
  -output_image ori/12_5.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_12 \
  -style_image $STYLE_6 \
  -output_image ori/12_6.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_12 \
  -style_image $STYLE_7 \
  -output_image ori/12_7.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_12 \
  -style_image $STYLE_8 \
  -output_image ori/12_8.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_12 \
  -style_image $STYLE_9 \
  -output_image ori/12_9.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_12 \
  -style_image $STYLE_10 \
  -output_image ori/12_10.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_12 \
  -style_image $STYLE_11 \
  -output_image ori/12_11.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_12 \
  -style_image $STYLE_12 \
  -output_image ori/12_12.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_12 \
  -style_image $STYLE_13 \
  -output_image ori/12_13.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_12 \
  -style_image $STYLE_14 \
  -output_image ori/12_14.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_12 \
  -style_image $STYLE_15 \
  -output_image ori/12_15.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_13 \
  -style_image $STYLE_1 \
  -output_image ori/13_1.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_13 \
  -style_image $STYLE_2 \
  -output_image ori/13_2.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_13 \
  -style_image $STYLE_3 \
  -output_image ori/13_3.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_13 \
  -style_image $STYLE_4 \
  -output_image ori/13_4.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_13 \
  -style_image $STYLE_5 \
  -output_image ori/13_5.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_13 \
  -style_image $STYLE_6 \
  -output_image ori/13_6.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_13 \
  -style_image $STYLE_7 \
  -output_image ori/13_7.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_13 \
  -style_image $STYLE_8 \
  -output_image ori/13_8.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_13 \
  -style_image $STYLE_9 \
  -output_image ori/13_9.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_13 \
  -style_image $STYLE_10 \
  -output_image ori/13_10.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_13 \
  -style_image $STYLE_11 \
  -output_image ori/13_11.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_13 \
  -style_image $STYLE_12 \
  -output_image ori/13_12.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_13 \
  -style_image $STYLE_13 \
  -output_image ori/13_13.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_13 \
  -style_image $STYLE_14 \
  -output_image ori/13_14.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_13 \
  -style_image $STYLE_15 \
  -output_image ori/13_15.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_14 \
  -style_image $STYLE_1 \
  -output_image ori/14_1.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_14 \
  -style_image $STYLE_2 \
  -output_image ori/14_2.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_14 \
  -style_image $STYLE_3 \
  -output_image ori/14_3.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_14 \
  -style_image $STYLE_4 \
  -output_image ori/14_4.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_14 \
  -style_image $STYLE_5 \
  -output_image ori/14_5.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_14 \
  -style_image $STYLE_6 \
  -output_image ori/14_6.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_14 \
  -style_image $STYLE_7 \
  -output_image ori/14_7.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_14 \
  -style_image $STYLE_8 \
  -output_image ori/14_8.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_14 \
  -style_image $STYLE_9 \
  -output_image ori/14_9.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_14 \
  -style_image $STYLE_10 \
  -output_image ori/14_10.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_14 \
  -style_image $STYLE_11 \
  -output_image ori/14_11.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_14 \
  -style_image $STYLE_12 \
  -output_image ori/14_12.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_14 \
  -style_image $STYLE_13 \
  -output_image ori/14_13.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_14 \
  -style_image $STYLE_14 \
  -output_image ori/14_14.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_14 \
  -style_image $STYLE_15 \
  -output_image ori/14_15.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_15 \
  -style_image $STYLE_1 \
  -output_image ori/15_1.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_15 \
  -style_image $STYLE_2 \
  -output_image ori/15_2.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_15 \
  -style_image $STYLE_3 \
  -output_image ori/15_3.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_15 \
  -style_image $STYLE_4 \
  -output_image ori/15_4.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_15 \
  -style_image $STYLE_5 \
  -output_image ori/15_5.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_15 \
  -style_image $STYLE_6 \
  -output_image ori/15_6.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_15 \
  -style_image $STYLE_7 \
  -output_image ori/15_7.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_15 \
  -style_image $STYLE_8 \
  -output_image ori/15_8.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_15 \
  -style_image $STYLE_9 \
  -output_image ori/15_9.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_15 \
  -style_image $STYLE_10 \
  -output_image ori/15_10.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_15 \
  -style_image $STYLE_11 \
  -output_image ori/15_11.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_15 \
  -style_image $STYLE_12 \
  -output_image ori/15_12.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_15 \
  -style_image $STYLE_13 \
  -output_image ori/15_13.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_15 \
  -style_image $STYLE_14 \
  -output_image ori/15_14.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_15 \
  -style_image $STYLE_15 \
  -output_image ori/15_15.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_16 \
  -style_image $STYLE_1 \
  -output_image ori/16_1.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_16 \
  -style_image $STYLE_2 \
  -output_image ori/16_2.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_16 \
  -style_image $STYLE_3 \
  -output_image ori/16_3.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_16 \
  -style_image $STYLE_4 \
  -output_image ori/16_4.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_16 \
  -style_image $STYLE_5 \
  -output_image ori/16_5.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_16 \
  -style_image $STYLE_6 \
  -output_image ori/16_6.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_16 \
  -style_image $STYLE_7 \
  -output_image ori/16_7.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_16 \
  -style_image $STYLE_8 \
  -output_image ori/16_8.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_16 \
  -style_image $STYLE_9 \
  -output_image ori/16_9.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_16 \
  -style_image $STYLE_10 \
  -output_image ori/16_10.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_16 \
  -style_image $STYLE_11 \
  -output_image ori/16_11.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_16 \
  -style_image $STYLE_12 \
  -output_image ori/16_12.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_16 \
  -style_image $STYLE_13 \
  -output_image ori/16_13.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_16 \
  -style_image $STYLE_14 \
  -output_image ori/16_14.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_16 \
  -style_image $STYLE_15 \
  -output_image ori/16_15.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_17 \
  -style_image $STYLE_1 \
  -output_image ori/17_1.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_17 \
  -style_image $STYLE_2 \
  -output_image ori/17_2.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_17 \
  -style_image $STYLE_3 \
  -output_image ori/17_3.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_17 \
  -style_image $STYLE_4 \
  -output_image ori/17_4.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_17 \
  -style_image $STYLE_5 \
  -output_image ori/17_5.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_17 \
  -style_image $STYLE_6 \
  -output_image ori/17_6.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_17 \
  -style_image $STYLE_7 \
  -output_image ori/17_7.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_17 \
  -style_image $STYLE_8 \
  -output_image ori/17_8.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_17 \
  -style_image $STYLE_9 \
  -output_image ori/17_9.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_17 \
  -style_image $STYLE_10 \
  -output_image ori/17_10.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_17 \
  -style_image $STYLE_11 \
  -output_image ori/17_11.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_17 \
  -style_image $STYLE_12 \
  -output_image ori/17_12.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_17 \
  -style_image $STYLE_13 \
  -output_image ori/17_13.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_17 \
  -style_image $STYLE_14 \
  -output_image ori/17_14.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_17 \
  -style_image $STYLE_15 \
  -output_image ori/17_15.png \
  -backend cudnn -cudnn_autotune
$NEURAL_STYLE \
  -content_image $CONTENT_1 \
  -style_image $STYLE_1 \
  -output_image res/1_1.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_1 \
  -style_image $STYLE_2 \
  -output_image res/1_2.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_1 \
  -style_image $STYLE_3 \
  -output_image res/1_3.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_1 \
  -style_image $STYLE_4 \
  -output_image res/1_4.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_1 \
  -style_image $STYLE_5 \
  -output_image res/1_5.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_1 \
  -style_image $STYLE_6 \
  -output_image res/1_6.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_1 \
  -style_image $STYLE_7 \
  -output_image res/1_7.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_1 \
  -style_image $STYLE_8 \
  -output_image res/1_8.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_1 \
  -style_image $STYLE_9 \
  -output_image res/1_9.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_1 \
  -style_image $STYLE_10 \
  -output_image res/1_10.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_1 \
  -style_image $STYLE_11 \
  -output_image res/1_11.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_1 \
  -style_image $STYLE_12 \
  -output_image res/1_12.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_1 \
  -style_image $STYLE_13 \
  -output_image res/1_13.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_1 \
  -style_image $STYLE_14 \
  -output_image res/1_14.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_1 \
  -style_image $STYLE_15 \
  -output_image res/1_15.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_2 \
  -style_image $STYLE_1 \
  -output_image res/2_1.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_2 \
  -style_image $STYLE_2 \
  -output_image res/2_2.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_2 \
  -style_image $STYLE_3 \
  -output_image res/2_3.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_2 \
  -style_image $STYLE_4 \
  -output_image res/2_4.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_2 \
  -style_image $STYLE_5 \
  -output_image res/2_5.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_2 \
  -style_image $STYLE_6 \
  -output_image res/2_6.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_2 \
  -style_image $STYLE_7 \
  -output_image res/2_7.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_2 \
  -style_image $STYLE_8 \
  -output_image res/2_8.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_2 \
  -style_image $STYLE_9 \
  -output_image res/2_9.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_2 \
  -style_image $STYLE_10 \
  -output_image res/2_10.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_2 \
  -style_image $STYLE_11 \
  -output_image res/2_11.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_2 \
  -style_image $STYLE_12 \
  -output_image res/2_12.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_2 \
  -style_image $STYLE_13 \
  -output_image res/2_13.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_2 \
  -style_image $STYLE_14 \
  -output_image res/2_14.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_2 \
  -style_image $STYLE_15 \
  -output_image res/2_15.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_3 \
  -style_image $STYLE_1 \
  -output_image res/3_1.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_3 \
  -style_image $STYLE_2 \
  -output_image res/3_2.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_3 \
  -style_image $STYLE_3 \
  -output_image res/3_3.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_3 \
  -style_image $STYLE_4 \
  -output_image res/3_4.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_3 \
  -style_image $STYLE_5 \
  -output_image res/3_5.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_3 \
  -style_image $STYLE_6 \
  -output_image res/3_6.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_3 \
  -style_image $STYLE_7 \
  -output_image res/3_7.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_3 \
  -style_image $STYLE_8 \
  -output_image res/3_8.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_3 \
  -style_image $STYLE_9 \
  -output_image res/3_9.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_3 \
  -style_image $STYLE_10 \
  -output_image res/3_10.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_3 \
  -style_image $STYLE_11 \
  -output_image res/3_11.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_3 \
  -style_image $STYLE_12 \
  -output_image res/3_12.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_3 \
  -style_image $STYLE_13 \
  -output_image res/3_13.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_3 \
  -style_image $STYLE_14 \
  -output_image res/3_14.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_3 \
  -style_image $STYLE_15 \
  -output_image res/3_15.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_4 \
  -style_image $STYLE_1 \
  -output_image res/4_1.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_4 \
  -style_image $STYLE_2 \
  -output_image res/4_2.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_4 \
  -style_image $STYLE_3 \
  -output_image res/4_3.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_4 \
  -style_image $STYLE_4 \
  -output_image res/4_4.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_4 \
  -style_image $STYLE_5 \
  -output_image res/4_5.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_4 \
  -style_image $STYLE_6 \
  -output_image res/4_6.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_4 \
  -style_image $STYLE_7 \
  -output_image res/4_7.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_4 \
  -style_image $STYLE_8 \
  -output_image res/4_8.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_4 \
  -style_image $STYLE_9 \
  -output_image res/4_9.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_4 \
  -style_image $STYLE_10 \
  -output_image res/4_10.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_4 \
  -style_image $STYLE_11 \
  -output_image res/4_11.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_4 \
  -style_image $STYLE_12 \
  -output_image res/4_12.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_4 \
  -style_image $STYLE_13 \
  -output_image res/4_13.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_4 \
  -style_image $STYLE_14 \
  -output_image res/4_14.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_4 \
  -style_image $STYLE_15 \
  -output_image res/4_15.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_5 \
  -style_image $STYLE_1 \
  -output_image res/5_1.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_5 \
  -style_image $STYLE_2 \
  -output_image res/5_2.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_5 \
  -style_image $STYLE_3 \
  -output_image res/5_3.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_5 \
  -style_image $STYLE_4 \
  -output_image res/5_4.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_5 \
  -style_image $STYLE_5 \
  -output_image res/5_5.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_5 \
  -style_image $STYLE_6 \
  -output_image res/5_6.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_5 \
  -style_image $STYLE_7 \
  -output_image res/5_7.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_5 \
  -style_image $STYLE_8 \
  -output_image res/5_8.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_5 \
  -style_image $STYLE_9 \
  -output_image res/5_9.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_5 \
  -style_image $STYLE_10 \
  -output_image res/5_10.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_5 \
  -style_image $STYLE_11 \
  -output_image res/5_11.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_5 \
  -style_image $STYLE_12 \
  -output_image res/5_12.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_5 \
  -style_image $STYLE_13 \
  -output_image res/5_13.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_5 \
  -style_image $STYLE_14 \
  -output_image res/5_14.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_5 \
  -style_image $STYLE_15 \
  -output_image res/5_15.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_6 \
  -style_image $STYLE_1 \
  -output_image res/6_1.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_6 \
  -style_image $STYLE_2 \
  -output_image res/6_2.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_6 \
  -style_image $STYLE_3 \
  -output_image res/6_3.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_6 \
  -style_image $STYLE_4 \
  -output_image res/6_4.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_6 \
  -style_image $STYLE_5 \
  -output_image res/6_5.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_6 \
  -style_image $STYLE_6 \
  -output_image res/6_6.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_6 \
  -style_image $STYLE_7 \
  -output_image res/6_7.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_6 \
  -style_image $STYLE_8 \
  -output_image res/6_8.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_6 \
  -style_image $STYLE_9 \
  -output_image res/6_9.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_6 \
  -style_image $STYLE_10 \
  -output_image res/6_10.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_6 \
  -style_image $STYLE_11 \
  -output_image res/6_11.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_6 \
  -style_image $STYLE_12 \
  -output_image res/6_12.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_6 \
  -style_image $STYLE_13 \
  -output_image res/6_13.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_6 \
  -style_image $STYLE_14 \
  -output_image res/6_14.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_6 \
  -style_image $STYLE_15 \
  -output_image res/6_15.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_7 \
  -style_image $STYLE_1 \
  -output_image res/7_1.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_7 \
  -style_image $STYLE_2 \
  -output_image res/7_2.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_7 \
  -style_image $STYLE_3 \
  -output_image res/7_3.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_7 \
  -style_image $STYLE_4 \
  -output_image res/7_4.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_7 \
  -style_image $STYLE_5 \
  -output_image res/7_5.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_7 \
  -style_image $STYLE_6 \
  -output_image res/7_6.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_7 \
  -style_image $STYLE_7 \
  -output_image res/7_7.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_7 \
  -style_image $STYLE_8 \
  -output_image res/7_8.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_7 \
  -style_image $STYLE_9 \
  -output_image res/7_9.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_7 \
  -style_image $STYLE_10 \
  -output_image res/7_10.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_7 \
  -style_image $STYLE_11 \
  -output_image res/7_11.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_7 \
  -style_image $STYLE_12 \
  -output_image res/7_12.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_7 \
  -style_image $STYLE_13 \
  -output_image res/7_13.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_7 \
  -style_image $STYLE_14 \
  -output_image res/7_14.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_7 \
  -style_image $STYLE_15 \
  -output_image res/7_15.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_8 \
  -style_image $STYLE_1 \
  -output_image res/8_1.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_8 \
  -style_image $STYLE_2 \
  -output_image res/8_2.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_8 \
  -style_image $STYLE_3 \
  -output_image res/8_3.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_8 \
  -style_image $STYLE_4 \
  -output_image res/8_4.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_8 \
  -style_image $STYLE_5 \
  -output_image res/8_5.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_8 \
  -style_image $STYLE_6 \
  -output_image res/8_6.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_8 \
  -style_image $STYLE_7 \
  -output_image res/8_7.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_8 \
  -style_image $STYLE_8 \
  -output_image res/8_8.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_8 \
  -style_image $STYLE_9 \
  -output_image res/8_9.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_8 \
  -style_image $STYLE_10 \
  -output_image res/8_10.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_8 \
  -style_image $STYLE_11 \
  -output_image res/8_11.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_8 \
  -style_image $STYLE_12 \
  -output_image res/8_12.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_8 \
  -style_image $STYLE_13 \
  -output_image res/8_13.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_8 \
  -style_image $STYLE_14 \
  -output_image res/8_14.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_8 \
  -style_image $STYLE_15 \
  -output_image res/8_15.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_9 \
  -style_image $STYLE_1 \
  -output_image res/9_1.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_9 \
  -style_image $STYLE_2 \
  -output_image res/9_2.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_9 \
  -style_image $STYLE_3 \
  -output_image res/9_3.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_9 \
  -style_image $STYLE_4 \
  -output_image res/9_4.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_9 \
  -style_image $STYLE_5 \
  -output_image res/9_5.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_9 \
  -style_image $STYLE_6 \
  -output_image res/9_6.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_9 \
  -style_image $STYLE_7 \
  -output_image res/9_7.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_9 \
  -style_image $STYLE_8 \
  -output_image res/9_8.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_9 \
  -style_image $STYLE_9 \
  -output_image res/9_9.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_9 \
  -style_image $STYLE_10 \
  -output_image res/9_10.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_9 \
  -style_image $STYLE_11 \
  -output_image res/9_11.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_9 \
  -style_image $STYLE_12 \
  -output_image res/9_12.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_9 \
  -style_image $STYLE_13 \
  -output_image res/9_13.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_9 \
  -style_image $STYLE_14 \
  -output_image res/9_14.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_9 \
  -style_image $STYLE_15 \
  -output_image res/9_15.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_10 \
  -style_image $STYLE_1 \
  -output_image res/10_1.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_10 \
  -style_image $STYLE_2 \
  -output_image res/10_2.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_10 \
  -style_image $STYLE_3 \
  -output_image res/10_3.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_10 \
  -style_image $STYLE_4 \
  -output_image res/10_4.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_10 \
  -style_image $STYLE_5 \
  -output_image res/10_5.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_10 \
  -style_image $STYLE_6 \
  -output_image res/10_6.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_10 \
  -style_image $STYLE_7 \
  -output_image res/10_7.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_10 \
  -style_image $STYLE_8 \
  -output_image res/10_8.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_10 \
  -style_image $STYLE_9 \
  -output_image res/10_9.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_10 \
  -style_image $STYLE_10 \
  -output_image res/10_10.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_10 \
  -style_image $STYLE_11 \
  -output_image res/10_11.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_10 \
  -style_image $STYLE_12 \
  -output_image res/10_12.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_10 \
  -style_image $STYLE_13 \
  -output_image res/10_13.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_10 \
  -style_image $STYLE_14 \
  -output_image res/10_14.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_10 \
  -style_image $STYLE_15 \
  -output_image res/10_15.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_11 \
  -style_image $STYLE_1 \
  -output_image res/11_1.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_11 \
  -style_image $STYLE_2 \
  -output_image res/11_2.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_11 \
  -style_image $STYLE_3 \
  -output_image res/11_3.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_11 \
  -style_image $STYLE_4 \
  -output_image res/11_4.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_11 \
  -style_image $STYLE_5 \
  -output_image res/11_5.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_11 \
  -style_image $STYLE_6 \
  -output_image res/11_6.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_11 \
  -style_image $STYLE_7 \
  -output_image res/11_7.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_11 \
  -style_image $STYLE_8 \
  -output_image res/11_8.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_11 \
  -style_image $STYLE_9 \
  -output_image res/11_9.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_11 \
  -style_image $STYLE_10 \
  -output_image res/11_10.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_11 \
  -style_image $STYLE_11 \
  -output_image res/11_11.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_11 \
  -style_image $STYLE_12 \
  -output_image res/11_12.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_11 \
  -style_image $STYLE_13 \
  -output_image res/11_13.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_11 \
  -style_image $STYLE_14 \
  -output_image res/11_14.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_11 \
  -style_image $STYLE_15 \
  -output_image res/11_15.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_12 \
  -style_image $STYLE_1 \
  -output_image res/12_1.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_12 \
  -style_image $STYLE_2 \
  -output_image res/12_2.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_12 \
  -style_image $STYLE_3 \
  -output_image res/12_3.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_12 \
  -style_image $STYLE_4 \
  -output_image res/12_4.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_12 \
  -style_image $STYLE_5 \
  -output_image res/12_5.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_12 \
  -style_image $STYLE_6 \
  -output_image res/12_6.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_12 \
  -style_image $STYLE_7 \
  -output_image res/12_7.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_12 \
  -style_image $STYLE_8 \
  -output_image res/12_8.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_12 \
  -style_image $STYLE_9 \
  -output_image res/12_9.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_12 \
  -style_image $STYLE_10 \
  -output_image res/12_10.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_12 \
  -style_image $STYLE_11 \
  -output_image res/12_11.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_12 \
  -style_image $STYLE_12 \
  -output_image res/12_12.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_12 \
  -style_image $STYLE_13 \
  -output_image res/12_13.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_12 \
  -style_image $STYLE_14 \
  -output_image res/12_14.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_12 \
  -style_image $STYLE_15 \
  -output_image res/12_15.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_13 \
  -style_image $STYLE_1 \
  -output_image res/13_1.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_13 \
  -style_image $STYLE_2 \
  -output_image res/13_2.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_13 \
  -style_image $STYLE_3 \
  -output_image res/13_3.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_13 \
  -style_image $STYLE_4 \
  -output_image res/13_4.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_13 \
  -style_image $STYLE_5 \
  -output_image res/13_5.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_13 \
  -style_image $STYLE_6 \
  -output_image res/13_6.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_13 \
  -style_image $STYLE_7 \
  -output_image res/13_7.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_13 \
  -style_image $STYLE_8 \
  -output_image res/13_8.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_13 \
  -style_image $STYLE_9 \
  -output_image res/13_9.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_13 \
  -style_image $STYLE_10 \
  -output_image res/13_10.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_13 \
  -style_image $STYLE_11 \
  -output_image res/13_11.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_13 \
  -style_image $STYLE_12 \
  -output_image res/13_12.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_13 \
  -style_image $STYLE_13 \
  -output_image res/13_13.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_13 \
  -style_image $STYLE_14 \
  -output_image res/13_14.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_13 \
  -style_image $STYLE_15 \
  -output_image res/13_15.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_14 \
  -style_image $STYLE_1 \
  -output_image res/14_1.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_14 \
  -style_image $STYLE_2 \
  -output_image res/14_2.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_14 \
  -style_image $STYLE_3 \
  -output_image res/14_3.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_14 \
  -style_image $STYLE_4 \
  -output_image res/14_4.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_14 \
  -style_image $STYLE_5 \
  -output_image res/14_5.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_14 \
  -style_image $STYLE_6 \
  -output_image res/14_6.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_14 \
  -style_image $STYLE_7 \
  -output_image res/14_7.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_14 \
  -style_image $STYLE_8 \
  -output_image res/14_8.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_14 \
  -style_image $STYLE_9 \
  -output_image res/14_9.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_14 \
  -style_image $STYLE_10 \
  -output_image res/14_10.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_14 \
  -style_image $STYLE_11 \
  -output_image res/14_11.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_14 \
  -style_image $STYLE_12 \
  -output_image res/14_12.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_14 \
  -style_image $STYLE_13 \
  -output_image res/14_13.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_14 \
  -style_image $STYLE_14 \
  -output_image res/14_14.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_14 \
  -style_image $STYLE_15 \
  -output_image res/14_15.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_15 \
  -style_image $STYLE_1 \
  -output_image res/15_1.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_15 \
  -style_image $STYLE_2 \
  -output_image res/15_2.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_15 \
  -style_image $STYLE_3 \
  -output_image res/15_3.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_15 \
  -style_image $STYLE_4 \
  -output_image res/15_4.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_15 \
  -style_image $STYLE_5 \
  -output_image res/15_5.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_15 \
  -style_image $STYLE_6 \
  -output_image res/15_6.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_15 \
  -style_image $STYLE_7 \
  -output_image res/15_7.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_15 \
  -style_image $STYLE_8 \
  -output_image res/15_8.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_15 \
  -style_image $STYLE_9 \
  -output_image res/15_9.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_15 \
  -style_image $STYLE_10 \
  -output_image res/15_10.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_15 \
  -style_image $STYLE_11 \
  -output_image res/15_11.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_15 \
  -style_image $STYLE_12 \
  -output_image res/15_12.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_15 \
  -style_image $STYLE_13 \
  -output_image res/15_13.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_15 \
  -style_image $STYLE_14 \
  -output_image res/15_14.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_15 \
  -style_image $STYLE_15 \
  -output_image res/15_15.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_16 \
  -style_image $STYLE_1 \
  -output_image res/16_1.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_16 \
  -style_image $STYLE_2 \
  -output_image res/16_2.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_16 \
  -style_image $STYLE_3 \
  -output_image res/16_3.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_16 \
  -style_image $STYLE_4 \
  -output_image res/16_4.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_16 \
  -style_image $STYLE_5 \
  -output_image res/16_5.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_16 \
  -style_image $STYLE_6 \
  -output_image res/16_6.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_16 \
  -style_image $STYLE_7 \
  -output_image res/16_7.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_16 \
  -style_image $STYLE_8 \
  -output_image res/16_8.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_16 \
  -style_image $STYLE_9 \
  -output_image res/16_9.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_16 \
  -style_image $STYLE_10 \
  -output_image res/16_10.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_16 \
  -style_image $STYLE_11 \
  -output_image res/16_11.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_16 \
  -style_image $STYLE_12 \
  -output_image res/16_12.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_16 \
  -style_image $STYLE_13 \
  -output_image res/16_13.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_16 \
  -style_image $STYLE_14 \
  -output_image res/16_14.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_16 \
  -style_image $STYLE_15 \
  -output_image res/16_15.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_17 \
  -style_image $STYLE_1 \
  -output_image res/17_1.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_17 \
  -style_image $STYLE_2 \
  -output_image res/17_2.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_17 \
  -style_image $STYLE_3 \
  -output_image res/17_3.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_17 \
  -style_image $STYLE_4 \
  -output_image res/17_4.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_17 \
  -style_image $STYLE_5 \
  -output_image res/17_5.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_17 \
  -style_image $STYLE_6 \
  -output_image res/17_6.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_17 \
  -style_image $STYLE_7 \
  -output_image res/17_7.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_17 \
  -style_image $STYLE_8 \
  -output_image res/17_8.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_17 \
  -style_image $STYLE_9 \
  -output_image res/17_9.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_17 \
  -style_image $STYLE_10 \
  -output_image res/17_10.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_17 \
  -style_image $STYLE_11 \
  -output_image res/17_11.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_17 \
  -style_image $STYLE_12 \
  -output_image res/17_12.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_17 \
  -style_image $STYLE_13 \
  -output_image res/17_13.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_17 \
  -style_image $STYLE_14 \
  -output_image res/17_14.png \
  -backend cudnn -cudnn_autotune -improve_gram
$NEURAL_STYLE \
  -content_image $CONTENT_17 \
  -style_image $STYLE_15 \
  -output_image res/17_15.png \
  -backend cudnn -cudnn_autotune -improve_gram
