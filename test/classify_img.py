###################################################
#This function is used to execute classify task
#author: Lei Jiang
#Date:2016 1 28
#version:1.0
###################################################

from net import Net
import os
import shutil
import exceptions
from config import Parameters
import cv2
import numpy as np
import matplotlib.pyplot as plt
from Getlist import getlist
import copy

def vis_square(data):
    """Take an array of shape (n, height, width) or (n, height, width, 3)
       and visualize each (height, width) thing in a grid of size approx. sqrt(n) by sqrt(n)"""
    # normalize data for display
    data = (data - data.min()) / (data.max() - data.min())
    # force the number of filters to be square
    n = int(np.ceil(np.sqrt(data.shape[0])))
    padding = (((0, n ** 2 - data.shape[0]),
               (0, 1), (0, 1))                 # add some space between filters
               + ((0, 0),) * (data.ndim - 3))  # don't pad the last dimension (if there is one)
    data = np.pad(data, padding, mode='constant', constant_values=1)  # pad with ones (white)
    
    # tile the filters into an image
    data = data.reshape((n, n) + data.shape[1:]).transpose((0, 2, 1, 3) + tuple(range(4, data.ndim + 1)))
    data = data.reshape((n * data.shape[1], n * data.shape[3]) + data.shape[4:])
    plt.imshow(data); plt.axis('off')

'''
input imagelist and classlist to split images
'''
def classifyimage(imagepath,classlistpath):
    pa=Parameters()
    net=Net(pa)
    imglist=getlist(imagepath,1)
    classlist=getlist(classlistpath,1)
    for image in imglist:
        try:
            category,confid=net.category(image)
        except:
            print "skip this%s"%image
        else:
            classname=classlist[category]
            classpath=os.path.join(pa.output_path,classname)
            if not os.path.exists(classpath):
                os.makedirs(classpath)
            shutil.copy(image,classpath)

'''
input image and vis features
'''
def VisFea(imagepath,fea_blob):
    fea_data = net.extract_fea(imagepath,fea_blob)
    vis_square(fea_data)

def visualclassify(floderpath,classlist):
    '''this function is used to show classify result'''
    for floder in os.listdir(floderpath):
        imagepath=os.path.join(floderpath,floder)
        try:
            category,confid=net.sortresult(imagepath)
        except:
            print "skip this"
        else:
            yla=''
            for ca,co in zip(category,confid):
                classname=classlist[ca]
                yla=yla+classname+':'+str(co)+'\n'

            plt.figure(1)
            plt.imshow(plt.imread(imagepath))
            plt.ylabel(yla)
            plt.savefig(pa.test_path+'/'+floder)


def classifyoneimage(imagepath):
    try:
        #category,confidence=net.category_cv(imagepath)
        category,confidence=net.category_ycbcr_warp(imagepath)
    except:
        print "skip this"
    else:
        print category,confidence


def save_wrong_result(test_file,save_path):
    fw = open("wrong.txt",'w')
    content_list = open(test_file).read().split('\n')
    content_list.remove("")
    for i,content in enumerate(content_list):
        if content=="":
            continue
        if i % 1000 == 0:
            print "has processed %d/ %d" %(i,len(content_list))
        image_file,label = content.split()
        #category,confidence =net.category_cv(image_file)
        category,confidence =net.category_ycbcr_warp(image_file)
        if str(category) != label:
            image_name = os.path.splitext(os.path.basename(image_file))[0]
            save_name = image_name +"pre"+str(category)+"corr"+label+str(confidence[0][0])+".jpg"
            save_file = os.path.join(save_path,save_name)
            shutil.copy(image_file,save_file)
            print confidence[0][0]
            each_line = content+"\n"
            fw.write(each_line)

def ClassifyImages(image_file,save_path):
    image_list = open(image_file).read().split('\n')
    image_list.remove("")
    for i,image_file in enumerate(image_list):
        if image_file =="":
            continue
        if i %1000 == 0:
            print "has processed %d / %d" %(i,len(image_list))
        category,confidence =net.category_cv(image_file)
        if category == 1:
            print image_file,confidence
        
        save_sub_path = os.path.join(save_path,str(category))
        if not os.path.exists(save_sub_path):
            os.mkdir(save_sub_path)
        image_name = os.path.basename(image_file)
        save_file = os.path.join(save_sub_path,image_name)
        shutil.copy(image_file,save_file)


'''
test two class accuracy
'''
def test_accuracy(test_file,model=None):
    pa=Parameters()
    if model != None:
        pa.model = model 
    net_obj=Net(pa)
    
    content_list = open(test_file).read().split('\n')
    content_list.remove("")
    total_num = len(content_list)
    total_error = 0
    total_correct = 0
    fake_correct = 0
    real_correct = 0
    
    fake_number = 0
    real_number = 0

    for content in content_list:
        if content=="":
            continue
        image_file,label = content.split()
        if label == "0":
            fake_number += 1
        else:
            real_number +=1
            
        category,confidence=net_obj.category_cv(image_file)
        if str(category) == label:
            total_correct = total_correct+1
            if category == 0:
                fake_correct +=1
            else:
                real_correct+=1
        else:
            total_error += 1
    
    total_acc = total_correct*1.0/total_num
    real_correct_acc = real_correct*1.0/real_number
    fake_acc = fake_correct*1.0/fake_number
    
    print "total accuracy is:%d %d %f"%(total_correct,total_num,total_acc)
    print "fake accuracy is:%d %d %f"%(fake_correct,fake_number,fake_acc)
    print "real  acuuracy is:%d %d %f"%(real_correct,real_number,real_correct_acc)
    print "total error is: %d"%total_error
    return (total_acc,real_correct_acc,fake_acc)
    

def statis_acc(test_file,model_path):
    model_list = [m for m in os.listdir(model_path) if os.path.splitext(m)[1] == ".caffemodel"]
    best=0.0
    best_model = ""
    for model in model_list:
        model_file = os.path.join(model_path,model)
        total_acc,real_acc,fake_acc = test_accuracy(test_file,model_file)
        print("{},acc {},real acc {},fake acc {}".format(model_file,total_acc,real_acc,fake_acc))
        if best < total_acc:
            best = total_acc
            best_model = model_file
    print best_model

if __name__=="__main__":
    statis_acc("/opt/datasets/maskimages/test.txt","/opt/datasets/maskimages/models")
