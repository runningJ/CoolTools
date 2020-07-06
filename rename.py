'''
@Author: your name
@Date: 2020-03-15 09:32:23
@LastEditTime: 2020-03-15 09:32:24
@LastEditors: your name
@Description: In User Settings Edit
@FilePath: /code/CoolTools/rename.py
'''
import os
import shutil

def rename_one_folder(folder_path,name):
    image_list = [image for image in os.listdir(folder_path) if os.path.splitext(image)[1] in ['.png','.jpg','.PNG','JPEG','.JPG']]
    for idx,image in enumerate(image_list):
        ori_name = os.path.join(folder_path,image)
        new_name = name +str(idx)+ os.path.splitext(image)[1]
        new_file = os.path.join(folder_path,new_name)
        os.rename(ori_name,new_file)

def folder_change(folder_path):
    folder_list = os.listdir(folder_path)
    for folder in folder_list:
        sub_folder = os.path.join(folder_path,folder)
        rename_one_folder(sub_folder,folder)

def change_folder_name(folder_path,name,start):
    folder_list = os.listdir(folder_path)
    for idx,folder in enumerate(folder_list):
        sub_folder_path = os.path.join(folder_path,folder)
        new_folder_name = name +str(idx+start)
        new_folder_path = os.path.join(folder_path,new_folder_name)
        os.rename(sub_folder_path,new_folder_path)
        




if __name__ =='__main__':
    folder_change("/opt/datasets/maskimages/test")
    #change_folder_name("/opt/datasets/wineimages/images_temp/clean","wineimage",757)