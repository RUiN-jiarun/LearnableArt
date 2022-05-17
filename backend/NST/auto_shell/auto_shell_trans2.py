import glob
import os

content = 'pre'
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
fs = open('final2.sh', 'w')
# idx = 1
# style_idx = 1
for content in content_paths:
    content = content.replace('\\','/')
    content_idx = content.split('/')[1].split('_')[0]
    style_idx = content.split('/')[1].split('_')[1]
    pre_type = content.split('/')[1].split('_')[2]
    if pre_type == 'hmrgb.png':
        fs.write(f'CONTENT_{content_idx}_{style_idx}_1={content}\n')
    else:
        fs.write(f'CONTENT_{content_idx}_{style_idx}_2={content}\n')
    # idx = idx + 1
    # style_idx = style_idx + 1
    # if style_idx > len(style_paths):
    #     style_idx = 1
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

# for i in range(len(content_paths)):
#     for j in range(len(style_paths)):
#         fs.write(f'$NEURAL_STYLE \\\n')
#         fs.write(f'  -content_image $CONTENT_{i+1} \\\n')
#         fs.write(f'  -style_image $STYLE_{j+1} \\\n')
#         fs.write(f'  -output_image ori/{i+1}_{j+1}.png \\\n')
#         fs.write(f'  -backend cudnn -cudnn_autotune\n')

for i in range(17):
    for j in range(len(style_paths)):
        fs.write(f'$NEURAL_STYLE \\\n')
        fs.write(f'  -content_image $CONTENT_{i+1}_{j+1}_1 \\\n')
        fs.write(f'  -style_image $STYLE_{j+1} \\\n')
        fs.write(f'  -output_image postres/{i+1}_{j+1}_hmrgb.png \\\n')
        fs.write(f'  -backend cudnn -cudnn_autotune -improve_gram\n')

for i in range(17):
    for j in range(len(style_paths)):
        fs.write(f'$NEURAL_STYLE \\\n')
        fs.write(f'  -content_image $CONTENT_{i+1}_{j+1}_2 \\\n')
        fs.write(f'  -style_image $STYLE_{j+1} \\\n')
        fs.write(f'  -output_image postres/{i+1}_{j+1}_fdmlab.png \\\n')
        fs.write(f'  -backend cudnn -cudnn_autotune -improve_gram\n')

fs.close()

