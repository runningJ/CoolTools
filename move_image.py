'''
@Author: your name
@Date: 2020-02-21 20:50:51
@LastEditTime: 2020-02-21 20:54:38
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /code/CoolTools/move_image.py
'''

import os
import shutil
from tqdm import tqdm

def MoveAccordFile(file_path,save_folder):
    fo = open(file_path)
    image_list = fo.read().split("\n")
    total_number = len(image_list)
    for idx in tqdm(range(total_number)):
        image = image_list[idx]
        if os.path.exists(image):
            shutil.copy(image,save_folder)

if __name__ == "__main__":
    MoveAccordFile("/home/nemo/code/WineService/detect_error.txt","/opt/datasets/detect_error")