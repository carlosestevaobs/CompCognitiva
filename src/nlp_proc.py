import nltk
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

stopwords_nltk = nltk.corpus.stopwords.words('portuguese')
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
                list_content_ts.append(token)
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
    texto = str(list_pre)
    nlp = stanza.Pipeline(lang='pt')
    doc = nlp(texto)

    texto_lematize_stanza = []
    for i in doc.sentences:
        for word in i.words:
            # print(word.lemma)
            texto_lematize_stanza.append(word.lemma)
    resultado = ' '.join(texto_lematize_stanza)
    return resultado

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
      return resultado
