# -*- coding: utf-8 -*-

import cv2

def equalizeHistogram(url):    
    img = cv2.imread(url)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  
    equ = cv2.equalizeHist(gray)
    return equ

def borderDetection(url):       
    img = cv2.imread(url)        
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
    sobelx = cv2.Sobel(gray,cv2.CV_64F,1,0,ksize=5)
    sobely = cv2.Sobel(gray,cv2.CV_64F,0,1,ksize=5)       
    return sobelx + sobely  

def Gaussian(url):       
    img = cv2.imread(url)        
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
    blur = cv2.GaussianBlur(gray,(5,5),0)
    return blur  




