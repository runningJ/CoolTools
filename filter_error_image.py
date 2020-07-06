'''
@Author: your name
@Date: 2020-02-17 22:31:46
@LastEditTime: 2020-02-17 22:31:47
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /code/CoolTools/filter_error_image.py
'''
import os
import cv2

def filter_one_image(image_file):
    img = cv2.imread(image_file)
    if img == None:
        os.remove(image_file)

def filter_problem(folder_path):
    folder_list = os.listdir(folder_path)
    for idx,sub_folder in enumerate(folder_list):
        if idx % 100 == 0:
            print('has processed {},{}'.format(idx,len(folder_list)))
        sub_folder_path = os.path.join(folder_path,sub_folder)
        image_list = os.listdir(sub_folder_path)
        for image_file in image_list:
            image_path = os.path.join(sub_folder_path,image_file)
            filter_one_image(image_path)

if __name__ == '__main__':
    filter_problem('/opt/datasets/readwinelibrary')
        