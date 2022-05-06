import datetime
import logging as rel_log
import os
import shutil
from datetime import timedelta
from flask import *
from importlib_metadata import re

from preprocessing.utils.application import run as match
from preprocessing.core import Params
from postprocessing.color_transfer import color_trans
from postprocessing.palette_transfer import palette_trans
from postprocessing.mask_transfer import mask_trans
from srgan.sr import sr_image
# from NST.neural_style_jt import param_main as nst_jt      # Jittor reports bug on cudnn
from NST.neural_style import param_main as nst_pt

import io
import imageio
from PIL import Image, ImageFile
from automask.u2net import mask
import numpy as np

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
def hist_match_page():
    src = request.values.get('src')
    style = request.values.get('style')
    isSrc2Style = request.values.get('isSrc2Style')
    algorithm = request.values.get('algorithm')
    color_space = request.values.get('color_space')
    channels = request.values.get('channels')
    match_proportion = request.values.get('match_proportion')
    param = {}
    # http://127.0.0.1:5003/tmp/ct/xxxxx.jpg
    # ./tmp/ct/xxxxx.jpg
    # print(color_space)
    channels = channels.lstrip('[').rstrip(']')
    # print(channels)
    pid = ""
    if src and style:
        src_path = '.' + src[21:]
        style_path = '.' + style[21:]
        # pid = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S') + '_' + src_path[9:]
        if int(isSrc2Style):
            pid = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S') + '_' + src_path[9:]
            param = {"color_space": color_space, 
                    "source_path": src_path, 
                    "reference_path": style_path, 
                    "channels": "0,1,2", 
                    "result_path": "./tmp/match/match_" + pid, 
                    "verify_input": "False", 
                    "plot": "False",
                    "match_proportion": match_proportion}
        else:
            pid = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S') + '_' + style_path[9:]
            param = {"color_space": color_space, 
                    "source_path": style_path, 
                    "reference_path": src_path, 
                    "channels": "0,1,2", 
                    "result_path": "./tmp/match/match_" + pid, 
                    "verify_input": "False", 
                    "plot": "False",
                    "match_proportion": match_proportion}
        match(algorithm, Params(param))

        return jsonify({'status': 1,
                        'draw_url': 'http://127.0.0.1:5003/tmp/match/match_' + pid})

    return jsonify({'status': 0})

@app.route('/automask', methods=['GET'])
def auto_mask_page():
    src = request.values.get('src')
    style = request.values.get('style')
    isSrc = request.values.get('isSrc')
    isBackground = request.values.get('isBackground')
    model_name = request.values.get('model')
    # http://127.0.0.1:5003/tmp/ct/xxxxx.jpg
    # ./tmp/ct/xxxxx.jpg
    # print(isSrc)
    pid = ""
    if src and style:
        src_path = '.' + src[21:]
        style_path = '.' + style[21:]
        
        # print(src_path, style_path)
        # test -- hard-coded
        # shutil.copy(src_path, './tmp/draw')
        if int(isSrc):
            if src_path.endswith('.jpg'):
                ImageFile.LOAD_TRUNCATED_IMAGES = True

            f = np.fromfile(src_path)
            # print(isBackground)
            res = mask.generate(f, model_name=model_name, isBackground=int(isBackground), dilate_structure_size=1)
            img = Image.open(io.BytesIO(res)).convert("RGBA")

            pid = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S') + '_' + src_path[9:]
        else:
            if style_path.endswith('.jpg'):
                ImageFile.LOAD_TRUNCATED_IMAGES = True

            f = np.fromfile(style_path)
            res = mask.generate(f, model_name=model_name, isBackground=int(isBackground), dilate_structure_size=1)
            img = Image.open(io.BytesIO(res)).convert("RGBA")
            pid = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S') + '_' + style_path[9:]
        
        pid = pid.split('.')[0] + '.png'
        output_path = './tmp/mask/mask_' + pid
        print(output_path)
        img.save(output_path)
        return jsonify({'status': 1,
                        'draw_url': 'http://127.0.0.1:5003/tmp/mask/mask_' + pid})

    return jsonify({'status': 0})

@app.route('/colortransfer', methods=['GET'])
def color_transfer_page():
    src = request.values.get('src')
    ref = request.values.get('ref')
    isMasked = request.values.get('isMasked')
    hist_match = request.values.get('hist_match')
    # http://127.0.0.1:5003/tmp/ct/xxxxx.jpg
    # ./tmp/ct/xxxxx.jpg
    # print(hist_match)
    if src and ref:
        src_path = '.' + src[21:]
        ref_path = '.' + ref[21:]
        pid = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S') + '_' + src_path[9:]
        img = color_trans(src_path, ref_path, isMasked, hist_match)
        output_path = './tmp/draw/colortrans_' + pid
        imageio.imwrite(output_path, img)
        # img = Image.fromarray(np.uint8(img))
        # img.save(output_path)
        return jsonify({'status': 1,
                        'draw_url': 'http://127.0.0.1:5003/tmp/draw/colortrans_' + pid})

    return jsonify({'status': 0})

@app.route('/palettetransfer', methods=['GET'])
def palette_transfer_page():
    src = request.values.get('src')
    target_h = request.values.get('target_h')
    # http://127.0.0.1:5003/tmp/ct/xxxxx.jpg
    # ./tmp/ct/xxxxx.jpg
    # print(hist_match)
    if src:
        src_path = '.' + src[21:]
        pid = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S') + '_' + src_path[9:]
        
        output_path = './tmp/draw/palettetrans_' + pid
        img = palette_trans(src_path, output_path, float(target_h))
        
        # img = Image.fromarray(np.uint8(img))
        # img.save(output_path)
        return jsonify({'status': 1,
                        'draw_url': 'http://127.0.0.1:5003/tmp/draw/palettetrans_' + pid})

    return jsonify({'status': 0})

@app.route('/automasktransfer', methods=['GET'])
def automask_transfer_page():
    src = request.values.get('src')
    ref = request.values.get('ref')
    isBackground = request.values.get('isBackground')
    model_name = request.values.get('model')
    # http://127.0.0.1:5003/tmp/ct/xxxxx.jpg
    # ./tmp/ct/xxxxx.jpg
    # print(hist_match)
    if src and ref:
        src_path = '.' + src[21:]
        ref_path = '.' + ref[21:]
        pid = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S') + '_' + src_path[9:]

        if ref_path.endswith('.jpg'):
            ImageFile.LOAD_TRUNCATED_IMAGES = True

        f = np.fromfile(ref_path)

        res = mask.generate(f, model_name=model_name, isBackground=int(isBackground), dilate_structure_size=1)
        content_mask = Image.open(io.BytesIO(res)).convert("RGBA")

        pid = pid.split('.')[0] + '.png'
        mask_path = './tmp/mask/mask_' + pid
        content_mask.save(mask_path)

        img = mask_trans(src_path, ref_path, mask_path)

        output_path = './tmp/draw/masktrans_' + pid
        imageio.imwrite(output_path, img)
        # img = Image.fromarray(np.uint8(img))
        # img.save(output_path)
        return jsonify({'status': 1,
                        'draw_url': 'http://127.0.0.1:5003/tmp/draw/masktrans_' + pid})

    return jsonify({'status': 0})

@app.route('/masktransfer', methods=['GET'])
def mask_transfer_page():
    src = request.values.get('src')
    ref = request.values.get('ref')
    mask = request.values.get('mask')
    # http://127.0.0.1:5003/tmp/ct/xxxxx.jpg
    # ./tmp/ct/xxxxx.jpg
    # print(hist_match)
    if src and ref:
        src_path = '.' + src[21:]
        ref_path = '.' + ref[21:]
        mask_path = '.' + mask[21:]
        pid = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S') + '_' + src_path[9:]

        img = mask_trans(src_path, ref_path, mask_path)

        output_path = './tmp/draw/masktrans_' + pid
        imageio.imwrite(output_path, img)
        # img = Image.fromarray(np.uint8(img))
        # img.save(output_path)
        return jsonify({'status': 1,
                        'draw_url': 'http://127.0.0.1:5003/tmp/draw/masktrans_' + pid})

    return jsonify({'status': 0})

@app.route('/nstjt', methods=['GET'])
def nst_jt_page():
    src = request.values.get('src')
    ref = request.values.get('ref')
    timeString = request.values.get('timeString')
    if src and ref:
        src_path = '.' + src[21:]
        ref_path = '.' + ref[21:]
        # global pid
        # pid = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S') + '_' + src_path[9:]
        pid = timeString + '_' + src_path[9:]
        output_path = './tmp/draw/trans_' + pid
        fname = src_path[9:].split('.')[0]
        ftype = src_path[9:].split('.')[1]
        # pid = timeString + '_' + src_path[9:]
        tmp_path_1 = timeString + '_' + fname + '_200.' + ftype
        tmp_path_2 = timeString + '_' + fname + '_400.' + ftype
        tmp_path_3 = timeString + '_' + fname + '_600.' + ftype
        tmp_path_4 = timeString + '_' + fname + '_800.' + ftype
        # TODO: NST Here
        # nst_jt(content_image=src_path, style_image=ref_path, output_image=output_path)
        return jsonify({'status': 1,
                        'draw_url': 'http://127.0.0.1:5003/tmp/draw/trans_' + pid})

    return jsonify({'status': 0})

@app.route('/nstpt', methods=['GET'])
def nst_pt_page():
    src = request.values.get('src')
    ref = request.values.get('ref')
    timeString = request.values.get('timeString')
    image_size = request.values.get('image_size')
    content_weight = request.values.get('content_weight')
    tv_weight = request.values.get('tv_weight')
    init = request.values.get('init')
    optimizer = request.values.get('optimizer')
    improve_gram = request.values.get('improve_gram')
    style_scale = request.values.get('style_scale')
    pooling = request.values.get('pooling')
    style_layers = request.values.get('style_layers')
    if src and ref:
        src_path = '.' + src[21:]
        ref_path = '.' + ref[21:]
        # global pid
        # pid = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S') + '_' + src_path[9:]
        pid = timeString + '_' + src_path[9:]
        output_path = './tmp/draw/trans_' + pid
        fname = src_path[9:].split('.')[0]
        ftype = src_path[9:].split('.')[1]
        # pid = timeString + '_' + src_path[9:]
        tmp_path_1 = timeString + '_' + fname + '_200.' + ftype
        tmp_path_2 = timeString + '_' + fname + '_400.' + ftype
        tmp_path_3 = timeString + '_' + fname + '_600.' + ftype
        tmp_path_4 = timeString + '_' + fname + '_800.' + ftype
        # TODO: NST Here
        if image_size:
            nst_pt(content_image=src_path, style_image=ref_path, output_image=output_path, image_size=int(image_size),
                    content_weight=float(content_weight),
                    tv_weight=float(tv_weight),
                    init=init,
                    optimizer=optimizer,
                    style_scale=float(style_scale),
                    pooling=pooling,
                    improve_gram=int(improve_gram),
                    style_layers_num=int(style_layers))
        else:
            nst_pt(content_image=src_path, style_image=ref_path, output_image=output_path)
        return jsonify({'status': 1,
                        'draw_url': 'http://127.0.0.1:5003/tmp/draw/trans_' + pid})

    return jsonify({'status': 0})

@app.route('/nsttmp', methods=['GET'])
def nst_tmp():
    src = request.args.get('src')
    timeString = request.args.get('timeString')
    # print(src, timeString)
    if src:
        src_path = '.' + src[21:]
        # pid = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S') + '_' + src_path[9:]
        fname = src_path[9:].split('.')[0]
        ftype = src_path[9:].split('.')[1]
        # pid = timeString + '_' + src_path[9:]
        tmp_path_1 = timeString + '_' + fname + '_200.' + ftype
        tmp_path_2 = timeString + '_' + fname + '_400.' + ftype
        tmp_path_3 = timeString + '_' + fname + '_600.' + ftype
        tmp_path_4 = timeString + '_' + fname + '_800.' + ftype

        data = {}
        data['status'] = 1

        if os.path.exists('tmp/draw/trans_' + tmp_path_4):
            data['tmp_url_4'] = 'http://127.0.0.1:5003/tmp/draw/trans_' + tmp_path_4
            return jsonify(data)
        if os.path.exists('tmp/draw/trans_' + tmp_path_3):
            data['tmp_url_3'] = 'http://127.0.0.1:5003/tmp/draw/trans_' + tmp_path_3
            return jsonify(data)
        if os.path.exists('tmp/draw/trans_' + tmp_path_2):
            data['tmp_url_2'] = 'http://127.0.0.1:5003/tmp/draw/trans_' + tmp_path_2
            return jsonify(data)
        if os.path.exists('tmp/draw/trans_' + tmp_path_1):
            data['tmp_url_1'] = 'http://127.0.0.1:5003/tmp/draw/trans_' + tmp_path_1
            return jsonify(data)
 

        # return jsonify({'status': 1,
        #                 'tmp_url_1': 'http://127.0.0.1:5003/tmp/draw/trans_' + tmp_path_1,
        #                 'tmp_url_2': 'http://127.0.0.1:5003/tmp/draw/trans_' + tmp_path_2,
        #                 'tmp_url_3': 'http://127.0.0.1:5003/tmp/draw/trans_' + tmp_path_3,
        #                 'tmp_url_4': 'http://127.0.0.1:5003/tmp/draw/trans_' + tmp_path_4})
        # return jsonify(data)

    return jsonify({'status': 0})

@app.route('/srgan', methods=['GET'])
def srgan_page():
    src = request.values.get('src')
    upscale_factor = request.values.get('upscale_factor')
    # http://127.0.0.1:5003/tmp/ct/xxxxx.jpg
    # ./tmp/ct/xxxxx.jpg
    pid = ""
    if src:
        src_path = '.' + src[21:]

        pid = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S') + '_' + src_path[9:]
        out_path = "./tmp/image/sr_" + upscale_factor + "_" + pid


        sr_image(upscale_factor=int(upscale_factor), image_path=src_path, out_path=out_path)

        return jsonify({'status': 1,
                        'draw_url': 'http://127.0.0.1:5003/tmp/image/sr_' + upscale_factor + "_" + pid})

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
        'tmp/image', 'tmp/mask', 'tmp/uploads', 'tmp/match'
    ]
    for ff in files:
        if not os.path.exists(ff):
            os.makedirs(ff)
    app.run(host='127.0.0.1', port=5003, threaded=True)
