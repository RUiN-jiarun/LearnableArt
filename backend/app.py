import datetime
import logging as rel_log
import os
import shutil
from datetime import timedelta
from flask import *

import io
from PIL import Image, ImageFile
from automask import u2net

UPLOAD_FOLDER = r'./uploads'

ALLOWED_EXTENSIONS = set(['png', 'jpg'])
app = Flask(__name__)
app.secret_key = 'secret!'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

werkzeug_logger = rel_log.getLogger('werkzeug')
werkzeug_logger.setLevel(rel_log.ERROR)

# 解决缓存刷新问题
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = timedelta(seconds=1)


# 添加header解决跨域
@app.after_request
def after_request(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Credentials'] = 'true'
    response.headers['Access-Control-Allow-Methods'] = 'POST'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type, X-Requested-With'
    return response


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route('/')
def hello_world():
    return redirect(url_for('static', filename='./index.html'))


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    file = request.files['file']
    # print(file)s
    print(datetime.datetime.now(), file.filename)
    if file and allowed_file(file.filename):
        src_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(src_path)
        shutil.copy(src_path, './tmp/ct')
        image_path = os.path.join('./tmp/ct', file.filename)
        pid= file.filename
        return jsonify({'status': 1,
                        'image_url': 'http://127.0.0.1:5003/tmp/ct/' + pid,
                        'draw_url': 'http://127.0.0.1:5003/tmp/ct/' + pid})

    return jsonify({'status': 0})

@app.route('/histmatch', methods=['GET'])
def hist_match():
    src = request.values.get('src')
    style = request.values.get('style')
    
    # http://127.0.0.1:5003/tmp/ct/xxxxx.jpg
    # ./tmp/ct/xxxxx.jpg
    
    if src and style:
        src_path = '.' + src[21:]
        style_path = '.' + style[21:]
        print(src_path, style_path)
        # test -- copy only
        shutil.copy(src_path, './tmp/draw')
    #     draw_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    #     file.save(draw_path)
    #     shutil.copy(draw_path, './tmp/draw')
    #     image_path = os.path.join('./tmp/draw', file.filename)
        pid= src_path[9:]
        # print(pid)
        return jsonify({'status': 1,
                        'draw_url': 'http://127.0.0.1:5003/tmp/draw/' + pid})

    return jsonify({'status': 0})

@app.route('/automask', methods=['GET'])
def auto_mask():
    src = request.values.get('src')
    style = request.values.get('style')
    
    # http://127.0.0.1:5003/tmp/ct/xxxxx.jpg
    # ./tmp/ct/xxxxx.jpg
    
    if src and style:
        src_path = '.' + src[21:]
        style_path = '.' + style[21:]
        
        # print(src_path, style_path)
        # test -- hard-coded
        # shutil.copy(src_path, './tmp/draw')
        res = u2net.mask.generate(src_path, model_name='u2netp', isBackground=False, dilate_structure_size=1)
        img = Image.open(io.BytesIO(res)).convert("RGBA")
        
    #     draw_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    #     file.save(draw_path)
    #     shutil.copy(draw_path, './tmp/draw')
    #     image_path = os.path.join('./tmp/draw', file.filename)
        pid= src_path[9:]
        
        output_path = './tmp/mask' + pid
        print(output_path)
        img.save(output_path)
        return jsonify({'status': 1,
                        'draw_url': 'http://127.0.0.1:5003/tmp/mask/' + pid})

    return jsonify({'status': 0})


@app.route("/download", methods=['GET'])
def download_file():
    # 需要知道2个参数, 第1个参数是本地目录的path, 第2个参数是文件名(带扩展名)
    return send_from_directory('data', 'testfile.zip', as_attachment=True)


# show photo
@app.route('/tmp/<path:file>', methods=['GET'])
def show_photo(file):
    if request.method == 'GET':
        if not file is None:
            image_data = open(f'tmp/{file}', "rb").read()
            response = make_response(image_data)
            response.headers['Content-Type'] = 'image/png'
            return response


if __name__ == '__main__':
    files = [
        'uploads', 'tmp/ct', 'tmp/draw',
        'tmp/image', 'tmp/mask', 'tmp/uploads'
    ]
    for ff in files:
        if not os.path.exists(ff):
            os.makedirs(ff)
    app.run(host='127.0.0.1', port=5003, debug=True)
