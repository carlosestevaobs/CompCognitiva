# -*- coding: utf-8 -*-
import sys
sys.path.insert(0, '../../')
from src.vc_proc import equalizeHistogram
import argparse
import cv2

def main():    
    ap  = argparse.ArgumentParser()
    ap.add_argument('-imagem', '--img',
                    default = "../../data_especular_crop/train_images/confluente/0.png",
                    help = 'primeiro ponto')
    

    args = vars(ap.parse_args())
    url = args['img']
    imagemEq = equalizeHistogram(url)
    print(imagemEq)
    cv2.imwrite('equalizada.png',imagemEq)
   

if __name__ == '__main__': 
    main()