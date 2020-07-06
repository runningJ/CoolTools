'''
@Author: your name
@Date: 2020-03-08 20:29:18
@LastEditTime: 2020-03-08 20:29:52
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /code/CoolTools/ImageAugment/image_aug.py
'''
import Augmentor
import os

def perspective_skewing(image_path,save_path):
    data_pipline = Augmentor.Pipeline(source_directory=image_path,output_directory=save_path)
    data_pipline.skew(probability=1.0,magnitude=0.2)
    data_pipline.sample(50)

def elastic_distoration(image_path,save_path):
    data_pipline = Augmentor.Pipeline(source_directory=image_path,output_directory=save_path)
    data_pipline.random_distortion(probability=1.0,grid_width=5,grid_height=5,magnitude=6)
    data_pipline.sample(50)

def random_erasing(image_path,save_path):
    data_pipline = Augmentor.Pipeline(source_directory=image_path,output_directory=save_path)
    data_pipline.random_erasing(probability=1.0,rectangle_area=0.2)
    data_pipline.process()

def rotate(image_path,save_path):
    data_pipline = Augmentor.Pipeline(source_directory=image_path,output_directory=save_path)
    data_pipline.rotate(probability=1.0,max_left_rotation = 45,max_right_rotation = 45)
    data_pipline.process()

def brightness(image_path,save_path):
    data_pipline = Augmentor.Pipeline(source_directory=image_path,output_directory=save_path)
    data_pipline.random_brightness(probability=1.0,min_factor=0.7,max_factor=1.5)
    data_pipline.process()

def resize(image_path,save_path):
    data_pipline = Augmentor.Pipeline(source_directory=image_path,output_directory=save_path)
    data_pipline.resize(probability=1.0,width=224,height=224)
    data_pipline.process()


'''
using this function to enlarge training images
'''
def augment_train(train_image,save_image):
    sub_folder_list = os.listdir(train_image)
    for sub_folder in sub_folder_list:
        sub_folder_path = os.path.join(train_image,sub_folder)
        save_path = os.path.join(save_image,sub_folder)
        #perspective_skewing(sub_folder_path,save_path)
        #elastic_distoration(sub_folder_path,save_path)
        #random_erasing(sub_folder_path,save_path)
        rotate(sub_folder_path,save_path)
        #brightness(sub_folder_path,save_path)

def augment_mask(train_image,save_image):
    sub_folder_list = os.listdir(train_image)
    for sub_folder in sub_folder_list:
        sub_folder_path = os.path.join(train_image,sub_folder)
        save_path = os.path.join(save_image,sub_folder)
        random_erasing(sub_folder_path,save_path)
        brightness(sub_folder_path,save_path)

        

if __name__ == "__main__":
    #augment_train("/opt/datasets/wineimages/winetrainimages/images","../../augments")
    augment_mask("/opt/datasets/maskimages/train20200308","../../augments20200308")
