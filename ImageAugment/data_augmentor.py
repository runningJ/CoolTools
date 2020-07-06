#coding:utf-8
#########################################################################
# File Name: data_augmentor.py
# Author:Lei Jiang
# mail: jianglei@1000look.com
# Created Time: 2016年04月12日 星期二 15时42分46秒
#########################################################################

from PIL import Image
from PIL import ImageEnhance
import numpy as np
import matplotlib.pyplot as plt
import cv2
from random import randint

class DataAugmentor(object):
    def __init__(self):
        pass
    def change_brightness(self,img_path,factor): #0.7
        '''change image brightness factor:0.0:black,1.0:original'''
        img=Image.open(img_path)
        img=img.convert('RGB')
        img_enhance=ImageEnhance.Brightness(img)
        res=img_enhance.enhance(factor)
        method_name='bright'
        return res, method_name

    def change_contrast(self,img_path,factor):
        '''change image contrast factor:0.0:solid grey image,1.0:original'''
        img=Image.open(img_path)
        img=img.convert('RGB')
        img_enhance=ImageEnhance.Contrast(img)
        res=img_enhance.enhance(factor)
        method_name='contrast'
        return res,method_name

    def change_sharpness(self,img_path,factor):
        '''change image sharpness factor:0.0 blured image,2.0 sharped image,1.0
        original'''
        img=Image.open(img_path)
        img=img.convert('RGB')
        img_enhance=ImageEnhance.Sharpness(img)
        res=img_enhance.enhance(factor)
        method_name='sharpness'
        return res,method_name
    
    def flip_image(self,img_path):
        img=Image.open(img_path)
        res=img.transpose(Image.FLIP_LEFT_RIGHT)
        method_name='flip'
        return res,method_name

    def change_color(self,img_path,factor):
        '''change image color factor:0.0 black and white 1.0 original'''
        img = Image.open(img_path)
        img = img.convert('RGB')
        img_enhance = ImageEnhance.Color(img)
        res = img_enhance.enhance(factor)
        method_name = 'color'
        return res,method_name

    def random_crop(self,img_path,factor):
        '''
        do random crop the edge of image
        '''
        img = cv2.imread(img_path)
        edge = randint(1,4) # 1 left 2 top 3 right 4 bottom
        crop_size = randint(1,factor)
        img_h,img_w,_ = img.shape

        if edge == 1:
            res = img[crop_size:img_h,:,:]
        elif edge ==2:
            res = img[:,crop_size:img_w,:]
        elif edge==3:
            res = img[:(img_h-crop_size),:,:]
        else:
            res = img[:,:(img_w - crop_size),:]
        method_name = 'random_crop'
        return res,method_name
    
    def random_earse(self,img_path,factor):
        '''
        do random earse the image
        '''
        img = cv2.imread(img_path)
        img_h,img_w,_ = img.shape

        bbox_h = randint(50,factor)
        bbox_w = randint(50,factor)

        start_x = randint(1,img_w - bbox_w -1)
        start_y = randint(1,img_h - bbox_h -1)

        method_name = "random_erase"
        img[start_y:start_y+bbox_h,start_x:start_x+bbox_w,:]=128

        return img,method_name

    def median_filter(self,img_path,factor):
        '''
        do median filter 
        '''
        img = cv2.imread(img_path)
        img_h,img_w,_ = img.shape
        method_name = "median_file"
        img = cv2.medianBlur(img,factor)
        return img,method_name
    def gaussian_filter(self,img_path,factor):
        '''
        do gaussian filter
        '''
        img = cv2.imread(img_path)
        img_h,img_w,_ = img.shape
        method_name = "gaussian_filter"
        img = cv2.GaussianBlur(img,(factor,factor),0)
        return img,method_name

    def blur_filter(self,img_path,factor):
        '''
        do blur filter
        '''
        img = cv2.imread(img_path)
        img_h,img_w,_ = img.shape
        method_name = "blur_filter"
        img = cv2.blur(img,(factor,factor))
        return img,method_name
    
    def shift_image(self,img_path,factor):
        '''
        do image shift
        '''
        img = cv2.imread(img_path)
        img_h,img_w,img_c = img.shape
        direction = randint(0,4)
        if direction ==0:
            new_img_w = img_w - factor
            new_img = np.zeros((img_h,new_img_w,img_c))
            new_img = img[:,factor:img_w,:]
        elif direction == 1:
            new_img_w = img_w - factor
            new_img = np.zeros((img_h,new_img_w,img_c))
            new_img = img[:,0:new_img_w,:]
        elif direction ==2:
            new_img_h = img_h - factor
            new_img = np.zeros((new_img_h,img_w,img_c))
            new_img = img[factor:img_h,:,:]
        else:
            new_img_h = img_h -factor
            new_img = np.zeros((new_img_h,img_w,img_c))
            new_img = img[0:new_img_h,:,:]

        method_name = "shift_image"
        return new_img,method_name

    def mix_up(self,front_img_path,bk_img_path,factor):
        front_img = cv2.imread(front_img_path)
        bk_img = cv2.imread(bk_img_path)
        resize_front_img = cv2.resize(front_img,(112,112))
        resize_bk_img = cv2.resize(bk_img,(112,112))
        mix_up_img = factor*resize_left_img+(1-factor)*resize_bk_img
        method_name = "mix_up"
        return mix_up_img,method_name
        
    def rotate_90(self,image_path,angle):
        img = cv2.imread(image_path)
        height, width = img.shape[:2]
        if width >height:
            return None,"no"

        img = cv2.resize(img,(224,224))
        matRotate = cv2.getRotationMatrix2D((height * 0.5, width * 0.5), angle, 1)
        dst = cv2.warpAffine(img, matRotate, (width*2, height*2))
        rows, cols = dst.shape[:2]
        for col in range(0, cols):
            if dst[:, col].any():
                left = col
                break
        for col in range(cols-1, 0, -1):
            if dst[:, col].any():
                right = col
                break
        for row in range(0, rows):
            if dst[row,:].any():
                up = row
                break
        for row in range(rows-1,0,-1):
            if dst[row,:].any():
                down = row
                break
        res_widths = abs(right - left)
        res_heights = abs(down - up)
        res = np.zeros([res_heights ,res_widths, 3], np.uint8)
        for res_width in range(res_widths):
            for res_height in range(res_heights):
                res[res_height, res_width] = dst[up+res_height, left+res_width]
        method_name = "rotate_90"
        return res,method_name




if __name__=="__main__":
    plt.subplot(121)
    ori=plt.imread('test.jpg')
    plt.imshow(ori)
##############################################
    da=DataAugmentor()
    res,_=da.gaussian_filter('test.jpg',21)
    res=res[:,:,(2,1,0)]
    res=np.array(res)
    plt.subplot(122)
    plt.imshow(res) 
    plt.show()
