#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 05 11:10:52 2021

@author: Estevao / Humberto Bezerra

"""    
def limiar(palavra, lista, limiar):
    
    lista_limiar = []
    indices_busca = lambda p,l: [i for i,e in enumerate(l) if e.lower().strip() == p] 
    
    limiar, palavra = int(limiar), str(palavra).lower().strip()

    for indice in indices_busca(palavra, lista):

        inicio = 0 if (limiar > indice) else (indice-limiar)
        
        lista_esq_indice = lista[inicio:indice]
        lista_dir_indice = lista[(indice+1):(indice+limiar+1)]
        
        lista_indice = lista_esq_indice + lista_dir_indice
        lista_limiar.extend([i for i in lista_indice if i not in lista_limiar and \
                                                        i != palavra])
    
    return lista_limiar   
