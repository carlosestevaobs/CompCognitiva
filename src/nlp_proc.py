# -*- coding: utf-8 -*-
import string
import csv
from collections import OrderedDict
import collections
import re
import nltk
import numpy as np
import stanza
from NLPyPort.FullPipeline import *

def lower_case(list_content):
    '''
   :param list_content_ts: lista dos conteúdos
   :return: lista dos conteúdos dos arquivos em letras minusculo (list_pre)
   '''
    list_lower = []
    for texto in list_content:
        setenca = texto.lower()
        list_lower.append(setenca)
    return list_lower

stopwords_nltk = nltk.corpus.stopwords.words('portuguese') + list(string.punctuation)
def remove_stopwords(list_content):
     '''
    :param list_content_tk: lista dos conteúdos
    :return: lista dos conteúdos com as stopwords removidas (list_content_ts)
    '''
     list_content_ts = []
     for i in range(len(list_content)):
        texto = list_content[i].split()
        for token in texto:
            if token not in stopwords_nltk:
                #result = re.sub('[^a-zA-Z]+', '', token)
                remove_numbers = re.sub(r'[0-9]+', '', token)
                remove_punctuation = re.compile('[%s]' % re.escape(string.punctuation  + '—'))
                result = remove_punctuation.sub(u'', remove_numbers)
                list_content_ts.append(result)
     resultado = ' '.join(list_content_ts)

     return resultado

def tokenizacao(list_content):
    '''
    :param list_content: lista dos conteúdos dos arquivos
    :return: lista dos conteúdos dos arquivos tokenizado (list_content_tk)
    '''
    list_content_tk = []
    for setenca in list_content:
        setenca_token = nltk.sent_tokenize(setenca)
        list_content_tk.append(setenca_token)

    return list_content_tk


def lematize_stanza(list_pre):
    '''
   :param list_pre: lista dos conteúdos dos arquivos tokenizado, stopwords removidas e letras em minusculo
   :return: lista dos conteúdos lematizados via lib stanza (list_pre_proc)
   '''
    #texto = str(list_pre)
    stanza.download('pt')
    nlp = stanza.Pipeline(lang='pt',tokenize_pretokenized=True,use_gpu= True)
    list_doc = []
    for texto in list_pre:
        doc = nlp(texto)
        list_doc.append(doc)

    texto_lematize_stanza = []
    for doc in list_doc:
        for i in doc.sentences:
            for word in i.words:
                # print(word.lemma)
                texto_lematize_stanza.append(word.lemma)
        #resultado = ' '.join(texto_lematize_stanza)
    return texto_lematize_stanza

def lematize_NLPyPort(list_pre):
      '''
     :param list_pre: lista dos conteúdos dos arquivos tokenizado, stopwords removidas e letras em minusculo
     :return: lista dos conteúdos lematizados via lib stanza (list_manual)
     '''
      options = {
          "tokenizer": True,
          "pos_tagger": True,
          "lemmatizer": True,
          "entity_recognition": True,
          "np_chunking": True,
          "pre_load": False,
          "string_or_array": True
      }

      text = new_full_pipe(list_pre, options=options)
      resultado = text.lemas
      resultado = [i for i in resultado if i.strip()!='EOS']
      return resultado


def extract_pdf(pathFile, file = None):
     '''
     :param list_pre: arquivo a ser extraido
     :return: lista com o conteúdo
     '''
     import fitz
     import traceback
     import pathlib

     content = []
     try:
         cover = str.maketrans({chr(10): '', chr(9): ''})
         dir = f'{pathFile}{file}' if file else (str(pathFile) + 'texto1.pdf')
         fp = pathlib.Path(dir)
         content = [p.get_text().translate(cover)  for p in fitz.open(fp)]

     except Exception as e:
         content = []
         print(f"{type(e).__name__} at line {e.__traceback__.tb_lineno} of {__file__}: {e}")

     return content



def extract_pdf_all(pathFile = '/'):
     '''
     :param list_pre: arquivo a ser extraido
     :return: lista com o conteúdo de 3 arquivos, se não encontrado posição exite mas vazia
     '''
     content_all = []
     for i in range(3):
         file = f'texto{(i+1)}.pdf'
         content = extract_pdf(pathFile, file)
         content_all.append(content)

     return content_all

if __name__ == '__main__':
    lista = extract_pdf_all()
    for i,p in enumerate(lista):
        print('**'*20,f'        Conteúdo do texto{i+1}.pdf        ','**'*20)
        print(p)
        print('**'*60)


def ordena_list(list_pre_proc):
    list_1 = []
    list_2 = []
    list_3 = []
    for aux, elemento in enumerate(list_pre_proc):
        for i in elemento:
            for j in i:
                if aux == 0:
                    list_1.append(j)
                if aux == 1:
                    list_2.append(j)
                if aux == 2:
                    list_3.append(j)
    list_1 = [' '.join(list_1)]
    list_2 = [' '.join(list_2)]
    list_3 = [' '.join(list_3)]

    return list_1, list_2, list_3

def createCSV(lista):

    cabecalho = ['doc', 'token', 'tf', 'df', 'idf', 'tf-idf']

    with open('base.csv', 'w', newline='', encoding='utf-16') as conteudo:
        write = csv.writer(conteudo)
        write.writerow(cabecalho)
        write.writerows(lista)

def df(list_pre_proc):
  '''
  :param list_pre_proc: lista dos conteúdos pré processados
  :retun: lista de tuplas com a palavra e seu valor df calculado(list_value_df)
  '''
  list_df = {}
  for indice in range(len(list_pre_proc)):
      doc = list_pre_proc[indice].split()
      for word in doc:
          if word not in list_df.keys():
              list_df[word] = 1
          else:
              list_df[word] += 1

  return list_df

def idf(list_df, list_pre_proc):
    '''
    :param list_pre_proc: lista dos conteúdos pré processados
    :param list_df: lista de document frequency
    :retun: lista de tuplas com a palavra e seu valor idf calculado(list_idf)
    '''
    list_idf = list_df
    for i in list_df:
        df = list_df[i]
        q_documento = len(list_pre_proc)
        idf = np.log((q_documento / df)+1)
        list_idf[i] = idf
    return list_idf

def tf(list_pre_proc):
    aux = [0,0,0]
    for count in range(3):
        doc = list_pre_proc[count].split()
        aux[count] = df(doc)

    tf = {}
    list_total = list_pre_proc[0] + list_pre_proc[1] + list_pre_proc[2]

    list_total = list(set(list_total.split()))
    for e in list_total:
        x = [0,0,0]
        for i in range(len(aux)):
            if e in list(aux[i].keys()):
                x[i] = (aux[i][e] / len(list_pre_proc[i].split()))
        tf.update({e:x})
    return tf

def tf_idf(tf, idf):
    tf_idf = {}
    for k, v in tf.items():
        if k in idf.keys():
            aux = idf[k]
        else:
            aux = 0
        for i in range(len(v)):
            v[i] = aux * v[i]
        tf_idf.update({k: v})
    return tf_idf


def top_five_tfidf(tf_idf):
    dic_total = {}
    for k, v in tf_idf.items():
        aux = sum(v)
        dic_total.update({k: aux})
    x = OrderedDict(sorted(dic_total.items(), key=lambda x: x[1], reverse=True))
    resulta_ordenado = []
    for e in x.keys():
        resulta_ordenado.append((e, x[e]))

    return resulta_ordenado[0:5]