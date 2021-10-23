# -*- coding: utf-8 -*-
"""
Created on Sat Oct 23 10:46:01 2021

@author: Estevao
"""
from collections import Counter
import numpy as np

def contar(lista):     
    valores = np.array(list(Counter(lista).values()))
    indices = np.array(list(Counter(lista).keys()))

    return np.column_stack((indices, valores))   
    
   
    