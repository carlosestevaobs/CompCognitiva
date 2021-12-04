# -*- coding: utf-8 -*-
import sys
sys.path.insert(0, '../../')

from src.nlp_proc import remove_stopwords

texto_exemplo = ['o câncer de pulmão é a doença maligna mais comum em todo o mundo; de todos os novos casos de câncer, 13% são de câncer de pulmão.(1) De acordo com o Global Burden of Disease Study 2015']

text_sem_stopwowrds = remove_stopwords(texto_exemplo)
print(text_sem_stopwowrds)
