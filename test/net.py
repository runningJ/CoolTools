'''
@Author: your name
@Date: 2020-03-15 10:49:07
@LastEditTime: 2020-03-15 10:50:23
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /code/CoolTools/test/net.py
'''

import numpy as np
from numpy import *
import sys
from skimage import transform
sys.path.insert(0,'/home/nemo/code/caffe/python')
import os  
os.environ['GLOG_minloglevel'] = '3'
import caffe
import exceptions
from sklearn import preprocessing
import cv2

class Net(object):
    def __init__(self,parameters):
        self.pa=parameters
        self.net=caffe.Net(self.pa.deploy_pt,self.pa.model,caffe.TEST)
        if self.pa.set_gpu:
            caffe.set_mode_gpu()
            caffe.set_device(self.pa.device_id)
        else:
            caffe.set_mode_cpu()

    def category_cv(self,imagepath):
        '''
        input image load using opencv and get category
        image value in [0 255]
        '''
        try:
            img = cv2.imread(imagepath)
            if img is None:
                return -1
        except:
            print("load image failed {}".format(imagepath))
        else:
            img = cv2.resize(img,(self.pa.shape[0],self.pa.shape[1]))
            img = img.astype(np.float64)
            img=img.transpose((2,0,1))
            self.net.blobs['data'].data[0]=img
            out=self.net.forward()
            category = out[self.pa.layer_name[0]][0].argmax()
            confidence = out[self.pa.layer_name[0]][0][category]
            return category,confidence