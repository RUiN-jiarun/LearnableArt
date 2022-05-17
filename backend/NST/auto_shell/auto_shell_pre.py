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
fs = open('pre.sh', 'w')
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
fs.write(f'SCRIPT=main.py\n')

fs.write(f'ISM=$PYTHON\n')
fs.write(f'ISM+=" "\n')
fs.write(f'ISM+=$SCRIPT\n')

for i in range(len(content_paths)):
    for j in range(len(style_paths)):
        fs.write(f'$ISM hm \\\n')
        fs.write(f'  -m 1.0 -s rgb -c 0,1,2 \\\n')
        fs.write(f'  $CONTENT_{i+1} $STYLE_{j+1} pre/{i+1}_{j+1}_hmrgb.png\n')

for i in range(len(content_paths)):
    for j in range(len(style_paths)):
        fs.write(f'$ISM fdm \\\n')
        fs.write(f'  -s lab -c 1,2 \\\n')
        fs.write(f'  $CONTENT_{i+1} $STYLE_{j+1} pre/{i+1}_{j+1}_fdmlab.png\n')