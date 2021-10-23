# -*- coding: utf-8 -*-
"""
Created on Sat Oct 23 09:17:17 2021

@author: Estevao
"""

import sys
sys.path.append('../src/')

from q2_distanciaEucl import calcDistEucl;
import argparse

def main():    
    ap  = argparse.ArgumentParser()
    ap.add_argument('-ponto', '--p1',
                    default = [1, 0, 3, 30],
                    help = 'primeiro ponto')
    
    ap.add_argument('-lista', '--lp',
                    default = [[19, 12, 19, 47], 
                               [8, 2, 9, 7], 
                               [5, 12, 8, 7], 
                               [1, 12, 5, 47]],
                    help = 'segundo ponto')    
    
    args = vars(ap.parse_args())
    ponto1 = args['p1']
    listaPontos = args['lp']    
  
    PontoMaisProximo = calcDistEucl(ponto1, listaPontos)
  
if __name__ == '__main__': 
    main()