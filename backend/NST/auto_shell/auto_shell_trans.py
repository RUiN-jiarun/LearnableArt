import glob
import os

content = 'content'
style = 'style'

if os.path.isfile(content):
    content_paths = [content]
else:
    content_paths = sorted(glob.glob(os.path.join(content, '*')))

if os.path.isfile(style):
    style_paths = [style]
else:
    style_paths = sorted(glob.glob(os.path.join(style, '*')))

# print(content_paths)
# print(style_paths)

# TODO: auto shell
fs = open('final.sh', 'w')
idx = 1
for content in content_paths:
    content = content.replace('\\','/')
    fs.write(f'CONTENT_{idx}={content}\n')
    idx = idx + 1
idx = 1
for style in style_paths:
    style = style.replace('\\','/')
    fs.write(f'STYLE_{idx}={style}\n')
    idx = idx + 1


fs.write(f'PYTHON=python3\n')
fs.write(f'SCRIPT=neural_style.py\n')

fs.write(f'NEURAL_STYLE=$PYTHON\n')
fs.write(f'NEURAL_STYLE+=" "\n')
fs.write(f'NEURAL_STYLE+=$SCRIPT\n')

"""
$NEURAL_STYLE \
  -content_image $CONTENT_IMAGE1_1 \
  -style_image $STYLE_IMAGE1 \
  -output_image res/hm_rgb_farmer.png \
  -backend cudnn -cudnn_autotune -improve_gram
"""

for i in range(len(content_paths)):
    for j in range(len(style_paths)):
        fs.write(f'$NEURAL_STYLE \\\n')
        fs.write(f'  -content_image $CONTENT_{i+1} \\\n')
        fs.write(f'  -style_image $STYLE_{j+1} \\\n')
        fs.write(f'  -output_image ori/{i+1}_{j+1}.png \\\n')
        fs.write(f'  -backend cudnn -cudnn_autotune\n')

for i in range(len(content_paths)):
    for j in range(len(style_paths)):
        fs.write(f'$NEURAL_STYLE \\\n')
        fs.write(f'  -content_image $CONTENT_{i+1} \\\n')
        fs.write(f'  -style_image $STYLE_{j+1} \\\n')
        fs.write(f'  -output_image res/{i+1}_{j+1}.png \\\n')
        fs.write(f'  -backend cudnn -cudnn_autotune -improve_gram\n')


fs.close()

