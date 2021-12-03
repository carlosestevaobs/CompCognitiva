import nltk

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
         # print(list_pre_exemplo[i])
         for sentencas in list_content[i]:
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