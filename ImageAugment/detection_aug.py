'''
Author: Lei Jiang
Email: leijiang420@163.com
Date: 2020-08-11 17:18:57
Description: code description
'''
from data_augmentor import DataAugmentor
import os
import cv2
import shutil

def BrightEnhance(folder_path,factor):
    str_factor = str(factor).replace('.','-')
    save_path = folder_path + "_bright_"+str_factor
    data_enhance = DataAugmentor()
    if not os.path.exists(folder_path):
        print("{} folder is not exists".format(folder_path))
    if not os.path.exists(save_path):
        os.mkdir(save_path)
    image_path = os.path.join(folder_path,'images')
    label_path = os.path.join(folder_path,'labels')
    save_image_path = os.path.join(save_path,'images')
    save_label_path = os.path.join(save_path,'labels')
    if not os.path.exists(save_image_path):
        os.mkdir(save_image_path)
    if not os.path.exists(save_label_path):
        os.mkdir(save_label_path)
    image_list = os.listdir(image_path)
    for image in image_list:
        image_file = os.path.join(image_path,image)
        label = os.path.splitext(image)[0]+".txt"
        label_file = os.path.join(label_path,label)
        res,_ = data_enhance.change_brightness(image_file,factor)
        save_image_file = os.path.join(save_image_path,image)
        res.save(save_image_file)
        shutil.copy(label_file,save_label_path)



def ContrastEnhance(folder_path,factor):
    str_factor = str(factor).replace('.','-')
    save_path = folder_path + "_contrast_"+str_factor
    data_enhance = DataAugmentor()
    if not os.path.exists(folder_path):
        print("{} folder is not exists".format(folder_path))
    if not os.path.exists(save_path):
        os.mkdir(save_path)
    image_path = os.path.join(folder_path,'images')
    label_path = os.path.join(folder_path,'labels')
    save_image_path = os.path.join(save_path,'images')
    save_label_path = os.path.join(save_path,'labels')
    if not os.path.exists(save_image_path):
        os.mkdir(save_image_path)
    if not os.path.exists(save_label_path):
        os.mkdir(save_label_path)
    image_list = os.listdir(image_path)
    for image in image_list:
        image_file = os.path.join(image_path,image)
        label = os.path.splitext(image)[0]+".txt"
        label_file = os.path.join(label_path,label)
        res,_ = data_enhance.change_contrast(image_file,factor)
        save_image_file = os.path.join(save_image_path,image)
        res.save(save_image_file)
        shutil.copy(label_file,save_label_path)



def EraseEnhance(folder_path,factor):
    str_factor = str(factor).replace('.','-')
    save_path = folder_path + "_erase_"+str_factor
    data_enhance = DataAugmentor()
    if not os.path.exists(folder_path):
        print("{} folder is not exists".format(folder_path))
    if not os.path.exists(save_path):
        os.mkdir(save_path)
    image_path = os.path.join(folder_path,'images')
    label_path = os.path.join(folder_path,'labels')
    save_image_path = os.path.join(save_path,'images')
    save_label_path = os.path.join(save_path,'labels')
    if not os.path.exists(save_image_path):
        os.mkdir(save_image_path)
    if not os.path.exists(save_label_path):
        os.mkdir(save_label_path)
    image_list = os.listdir(image_path)
    for image in image_list:
        image_file = os.path.join(image_path,image)
        label = os.path.splitext(image)[0]+".txt"
        label_file = os.path.join(label_path,label)
        res,_ = data_enhance.random_earse(image_file,factor)
        save_image_file = os.path.join(save_image_path,image)
        cv2.imwrite(save_image_file,res)
        shutil.copy(label_file,save_label_path)



if __name__ == '__main__':
    EraseEnhance("/home/nemo/datasets/safe_recognition_night/20200812",40)
    ContrastEnhance("/home/nemo/datasets/safe_recognition_night/20200812",1.3)
    BrightEnhance("/home/nemo/datasets/safe_recognition_night/20200812",1.2)