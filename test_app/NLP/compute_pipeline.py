import sys
sys.path.insert(0, '../../')
sys.path.insert(1,'../../document/NLP/')

from src.nlp_proc import extract_pdf_all
from src.nlp_proc import lower_case, remove_stopwords, tokenizacao
from src.nlp_proc import lematize_stanza, lematize_NLPyPort, df, idf, ordena_list


if __name__ == '__main__':
    dir = str(sys.path[1])
    lista = extract_pdf_all(dir)
    lista_pre = []
    lista_tokenizada = []
    for doc in lista:
        #print(type(doc))
        lista_pre.append(remove_stopwords(lower_case(doc)))
    for doc_t in lista_pre:
        lista_tokenizada.append(tokenizacao([doc_t]))

    list_stanza = []
    lista_manual = []
    for i, element in enumerate(lista_tokenizada):
        list_element_sentenca_stanza = []
        list_element_sentenca_manual = []
        for senteca in element:
            list_element_sentenca_manual.append(lematize_NLPyPort(senteca))
            list_element_sentenca_stanza.append(lematize_stanza(senteca))
        list_stanza.append(list_element_sentenca_stanza)
        lista_manual.append(list_element_sentenca_manual)

    list_1s, list_2s, list_3s = ordena_list(list_stanza)
    list_final_stanza = list_1s + list_2s + list_3s

    list_1m, list_2m, list_3m = ordena_list(lista_manual)
    list_final_manual = list_1m + list_2m + list_3m

    list_df_stanza = df(list_final_stanza)
    list_df_manual = df(list_final_manual)
    list_idf_stanza = idf(list_df_stanza,list_final_stanza)
    list_idf_manual = idf(list_df_manual,list_final_manual)


