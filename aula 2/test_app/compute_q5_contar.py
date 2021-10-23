# -*- coding: utf-8 -*-
"""
Created on Sat Oct 23 10:45:50 2021

@author: Estevao
"""

import sys
sys.path.append('../src/')

from q5_contar import contar;
import argparse

def main():    
    ap  = argparse.ArgumentParser()
    ap.add_argument('-lst', '--lista',
                    default = ['maçã', 'laranja', 'maçã','abacate', 'pêra', 'limão',
                               'maça', 'uva', 'maçã'],
                    help = 'Lista de Strings')   
    
    args = vars(ap.parse_args())  
    lista = args['lista']         
    
    NLista = contar(lista)      
  
if __name__ == '__main__': 
    main()