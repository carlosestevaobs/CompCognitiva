# -*- coding: utf-8 -*-
"""
Created on Sat Oct 23 10:03:02 2021

@author: Estevao
"""

import numpy as np

def calcDistEucl(ponto1, listaPontos):     
    ponto1 = np.array(ponto1)
    listaPontos = np.array(listaPontos)    
    
    '''
    A distância euclidiana é calculada por:
    distancia = raiz(somatorio((p1-p2)^2))
    ''' 
    distancia = []
    menorPosicao = 0
    for i in range(listaPontos.shape[0]):
        distancia.append(np.sqrt(np.sum(np.square(ponto1-listaPontos[i]))))
       
   
    return distancia[np.argmin(distancia)]
