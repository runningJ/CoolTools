#coding:utf-8
#########################################################################
# File Name: config.py
# Author:Lei Jiang
# mail: leijiang420@163.com
# Created Time: 2016年04月06日 星期三 14时48分00秒
# Copyright Nanjing Qing So information technology
#########################################################################

import numpy as np
from numpy import *

class Parameters(object):
    '''set Parameters for net'''
    def __init__(self):
        self.set_gpu=True
        self.device_id=0
        self.deploy_pt='/home/nemo/code/masktrain/deploy.prototxt'
        self.model = '/home/nemo/code/ncnn/build/tools/caffe/mask/mask_iter_120000.caffemodel'
        self.shape = [112,112,3]
        self.mean_value=np.array([127.5, 127.5, 127.5])
        self.layer_name = ['prob']




