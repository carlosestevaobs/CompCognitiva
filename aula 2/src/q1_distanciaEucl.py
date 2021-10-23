# -*- coding: utf-8 -*-
"""
Created on Sat Oct 23 08:20:38 2021

@author: Estevao
"""

import numpy as np

def calcDistEucl(p1, p2):     
    p1 = np.array(p1)
    p2 = np.array(p2)    
    
    '''
    A distância euclidiana é calculada por:
    distancia = raiz(somatorio((p1-p2)^2))
    ''' 
    distancia = np.sqrt(np.sum(np.square(p1-p2)))
    print("A distância entre os dois pontos é " + str(distancia))
