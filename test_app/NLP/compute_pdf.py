# -*- coding: utf-8 -*-
import sys
sys.path.insert(0, '../../')
sys.path.insert(1,'../../document/NLP/')

from src.nlp_proc import extract_pdf_all


if __name__ == '__main__':
    dir = str(sys.path[1])
    lista = extract_pdf_all(dir)
    for i,p in enumerate(lista):
        print('**'*20,f'        Conteúdo do texto{i+1}.pdf        ','**'*20)
        print(p)
        print('**'*60)
