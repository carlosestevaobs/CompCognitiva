import sys
sys.path.insert(0, '../../')
sys.path.insert(1,'../../document/NLP/')

from src.nlp_proc import extract_pdf_all
from src.nlp_proc import lower_case, remove_stopwords, tokenizacao
from src.nlp_proc import lematize_stanza, lematize_NLPyPort


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
    print(len(lista_tokenizada), lista_tokenizada[2])
    print(len(list_stanza), list_stanza[2])
    print(len(lista_manual), lista_manual[2])

