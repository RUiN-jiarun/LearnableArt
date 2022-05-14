import glob
import os
import torch
from PIL import Image
from pyiqa.models.inference_model import InferenceModel

def iqa(input, log_path):
    metric_list = ['niqe', 'ilniqe', 'brisque', 'nrqm', 'pi', 'musiq', 'nima', 'paq2piq', 'dbcnn']
    # metric_list = ['niqe', 'ilniqe', 'brisque', 'pi', 'musiq', 'nima', 'paq2piq', 'dbcnn']
    metric_mode = 'NR'
    # input = 'testing_res/adam_res'
    sf = open(log_path, 'w')
    if os.path.isfile(input):
        input_paths = [input]
    else:
        input_paths = sorted(glob.glob(os.path.join(input, '*.png')))

    for metric_name in metric_list:
        iqa_model = InferenceModel(metric_name, metric_mode)
        avg_score = 0
        test_img_num = len(input_paths)
        for idx, img_path in enumerate(input_paths):
            img_name = os.path.basename(img_path)
            tar_img = Image.open(img_path)
            score = iqa_model.test(tar_img)
            avg_score += score
            print(f'{metric_name} score of {img_name} is: {score}')
            sf.write(f'{img_name}\t\t{metric_name}\t{score}\n')
        avg_score /= test_img_num
        if test_img_num > 1:
            print(f'Average {metric_name} score of {input} with {test_img_num} images is: {avg_score}')
            sf.write(f'{metric_name} Average score: {avg_score}\n\n')
        torch.cuda.empty_cache()
    print(f'Done!')
    sf.close()

if __name__ == '__main__':
    iqa(input='testing_res/adam_res', log_path='adam_log.txt')