'''
Author: Lei Jiang
Email: leijiang420@163.com
Date: 2020-08-07 16:15:45
Description: code description
'''
import os
import cv2
import shutil

def color2gray(image_file):
    img = cv2.imread(image_file)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return img_gray

def ColorToGray(folder_path,save_path):
    #check folder 
    if not os.path.exists(save_path):
        os.mkdir(save_path)
    save_image_folder = os.path.join(save_path,"images")
    save_label_folder = os.path.join(save_path,"labels")
    if not os.path.exists(save_image_folder):
        os.mkdir(save_image_folder)
    if not os.path.exists(save_label_folder):
        os.mkdir(save_label_folder)

    image_folder = os.path.join(folder_path,"images")
    label_folder = os.path.join(folder_path,"labels")

    image_list = os.listdir(image_folder)
    image_number = len(image_list)
    for idx in range(image_number):
        image_file = image_list[idx]
        image_path = os.path.join(image_folder,image_file)
        img_gray = color2gray(image_path)
        save_image_path = os.path.join(save_image_folder,image_file)
        cv2.imwrite(save_image_path,img_gray)
        label_file = image_file.replace(os.path.splitext(image_file)[1],".txt")
        label_path = os.path.join(label_folder,label_file)
        shutil.copy(label_path,save_label_folder)

def ImageToGray(folder_path,save_folder):
    image_list = [image for image in os.listdir(folder_path) if os.path.splitext(image)[1] in ['.jpg','.png','.jpeg']]
    for image in image_list:
        image_file = os.path.join(folder_path,image)
        image_gray = color2gray(image_file)
        save_image_file = os.path.join(save_folder,image)
        cv2.imwrite(save_image_file,image_gray)

if __name__=="__main__":
    ImageToGray("/home/nemo/datasets/20200807/images","/home/nemo/datasets/20200807/grayimages")
    
