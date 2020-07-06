#coding:utf-8
#########################################################################
# File Name: Getlist.py
# Author:
# mail: 
# Created Time: 2016年04月07日 星期四 11时18分14秒
# Copyright Nanjing Qing So information technology
#########################################################################
def getlist(txtpath,n):
    '''get lit from text, txtpath is the path of .txt, n is used to adapt
    window and linux'''
    with open(txtpath) as f:
        classlist=f.readlines()
        newlist=[]
        for str in classlist:
            strlen=len(str)
            str=str[:strlen-n]
            newlist.append(str)
        return newlist


