import sys
sys.path.insert(0, '../../')

from src.nlp_proc import tokenizacao

texto_exemplo = ['o câncer de pulmão é a doença maligna mais comum em todo o mundo; de todos os novos casos de câncer, 13% são de câncer de pulmão.(1) De acordo com o Global Burden of Disease Study 2015']

text_tokenizado = tokenizacao(texto_exemplo)
print(text_tokenizado)