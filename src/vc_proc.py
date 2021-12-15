# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 08:27:46 2021

@author: Estevao
"""


import cv2

def equalizeHistogram(url):    
    img = cv2.imread(url)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  
    equ = cv2.equalizeHist(gray)
    return equ

# para teste de visualização de diferença
#image = equalizeHistogram("../data_especular_crop/train_images/confluente/0.png")
#cv2.imwrite('equalizada.png',image)

def borderDetection(url):       
    img = cv2.imread(url)        
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
    sobelx = cv2.Sobel(gray,cv2.CV_64F,1,0,ksize=5)
    sobely = cv2.Sobel(gray,cv2.CV_64F,0,1,ksize=5)       
    return sobelx + sobely  
    
#image = borderDetection("../data_especular_crop/train_images/confluente/0.png")
#cv2.imwrite('borda.png',image)


def Gaussian(url):       
    img = cv2.imread(url)        
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
    blur = cv2.GaussianBlur(gray,(5,5),0)
    return blur  
    
#image = Gaussian("../data_especular_crop/train_images/confluente/0.png")
#cv2.imwrite('blur.png',image)



