# -*- coding: utf-8 -*-
"""
Created on Sat Oct 23 09:28:01 2021

@author: Estevao
"""

import sys
sys.path.append('../src/')

from q10_limiarizar import limiarizar;
import numpy as np
import argparse

def main():        
    ap  = argparse.ArgumentParser()
    ap.add_argument('-M', '--mat',
                    default = np.random.randint(0,255,(10,10)),
                    help = 'Matriz')    
    
    ap.add_argument('-v', '--valor',
                    default = 100,
                    help = 'Valor')    
    
    
    args = vars(ap.parse_args())
    matriz = args['mat']
    valor =  args['valor']

    limiarizar(matriz, valor)
  
if __name__ == '__main__': 
    main()