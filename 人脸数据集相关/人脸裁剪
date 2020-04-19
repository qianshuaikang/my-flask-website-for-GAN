# -*- coding: utf-8 -*-
"""
Spyder Editor
This is a temporary script file.
"""

import os
import cv2
import glob
from PIL import Image
from PIL import ImageFile
import threading
import numpy as np
size_m=512#裁剪后图片的宽
size_n=512#裁剪后图片的高
## 读取图像，解决imread不能读取中文路径的问题    
def cv_imread(file_path):
    cv_img = cv2.imdecode(np.fromfile(file_path,dtype=np.uint8),-1)
    return cv_img
def tailor(img,x,y,w,h,a,b,c,d):#裁剪人脸函数
    x1=int(x*a)#根据人脸调整人脸检测框左顶点x,y坐标，a,b是缩放系数
    y1=int(y*b)
    w1=int(x + c*w)#根据人脸来调整人脸框的长宽
    h1=int(y +d*h)
    #img = cv2.rectangle(img, (x1, y1),( w1,h1), (255, 0, 0), 2)
    roi_color = img[y1: h1, x1: w1]#选取人脸区域
    return roi_color  #返回人脸图像
path="E:\\GAN_image"#图片文件的根目录
target_path="E:\\GAN_image\\taiwan"#保存裁剪后图片的目录
images=glob.glob(os.path.join(path,"*\\*.jpg"))#读取根目录下所有
face_cascade = cv2.CascadeClassifier(r"E:\Anaconda3\Lib\site-packages\cv2\data\haarcascade_frontalface_alt2.xml")#opencv里自带的人脸识别分类器,.xml文件的路径根据自己的下载地址改写
if not os.path.exists(target_path):#裁剪后的图片的路径
    os.mkdir(target_path)
num=0#图片名字的数字，会根据num.jpg来改名字
for i,list1 in enumerate(images):  #枚举图片路径
    if i is len(images)-1:
        break
    else:
        try:    
            img=cv_imread(list1) #读取单个图片
            gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)#将彩色图片转为灰度图
            faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(30, 30),flags=cv2.CASCADE_SCALE_IMAGE)#将灰度图放入人脸检测器，提高效率
            if len(faces) is not 1:#如果只有不止一个人脸，跳过
                continue
            else:#只有一个人脸，做裁剪操作
                for (x,y,w,h) in faces:#读取人脸的坐标和宽高
                    if  w>img.shape[1]/3:  #因为有的图片人脸比较大，有的人脸比较小，根据人脸占整个图片的大小来调整缩放系数a,b,c,d
                        new_img=tailor(img,x,y,w,h,1/3,1/3,1.28,1.28) #裁剪人脸，当中的系数并非最有,可以根据自己的需要修改
                    else:
                        new_img=tailor(img,x,y,w,h,0.7,0.6,1.35,1.3)
                renew_img = cv2.resize(new_img, (size_m, size_n))#将图片重新改为m*n大小
                cv2.imwrite("{}\\{}.jpg".format(target_path,num), renew_img)#保存图片到目标路径
                num+=1#nun.jpg
                #cv2.imshow('img',renew_img)
                #k=cv2.waitKey(0)
                #cv2.destroyAllWindows()
        except:
            continue
