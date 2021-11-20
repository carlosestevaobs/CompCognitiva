# Atividade a serem desenvolvidas durante a implementação de NLP:

## 1° - Carregar o conjunto de documentos em PDF e armazená-los em alguma estrutura de dados 
```
def Load_pdf (list_files):
    '''
    :param list_files: lisa de arquivos
    :return: lista dos conteúdos dos arquivos (list_content)
    '''
```

## 2° - Realizar o pré-processamento destes ( tokenização e remoção de stop words, deixar todos os caracteres minúsculos...)
```
def tokenizacao(list_content):
    '''
    :param list_content: lista dos conteúdos dos arquivos
    :return: lista dos conteúdos dos arquivos tokenizado (list_content_tk)
    '''
def remove_stopwords(list_content_tk):
     '''
    :param list_content_tk: lista dos conteúdos dos arquivos tokenizado (list_content_tk)
    :return: lista dos conteúdos dos arquivos tokenizado e com as stopwords removidas (list_content_ts)
    '''
def lower_case(list_content_ts):
     '''
    :param list_content_ts: lista dos conteúdos dos arquivos tokenizado e com as stopwords removidas (list_content_ts)
    :return: lista dos conteúdos dos arquivos tokenizado, stopwords removidas e letras em minusculo (list_pre)
    '''
```

## 3° - Lematização com a Lib stanza
```
def lematize_stanza(list_pre):
     '''
    :param list_pre: lista dos conteúdos dos arquivos tokenizado, stopwords removidas e letras em minusculo
    :return: lista dos conteúdos lematizados via lib stanza (list_pre_proc)
    '''
```

## 4° - Lematização manual com inspiração no trabalho descrito no link seguinte (Atividade desafio):
    https://github.com/rikarudo/LemPORT 
   ```
  def lematize_manual(list_pre):
     '''
    :param list_pre: lista dos conteúdos dos arquivos tokenizado, stopwords removidas e letras em minusculo
    :return: lista dos conteúdos lematizados via lib stanza (list_manual)
    '''
  ```
  
## 5° - Implementar API para determinar as seguintes informações do resultados obtidos nas atividades 3 e/ou 4 :
```
def api(list_pre_proc):
   '''
   :param list_pre_proc: lista dos conteúdos pré processados
   :return: retorna os resultado das operações (resultados.json)
   {"tf":list_value_tf, "df": list_value_df, "idf":list_value_idf, "tf-idf":list_value_tfidf, "list_tf":list_string_tf}
   '''
   
def tf(list_pre_proc):
  '''
  :param list_pre_proc: lista dos conteúdos pré processados
  :retun: lista de tuplas com a palavra e seu valor tf calculado (list_value_tf)
  '''
def df(list_pre_proc):
  '''
  :param list_pre_proc: lista dos conteúdos pré processados
  :retun: lista de tuplas com a palavra e seu valor df calculado(list_value_df)
  '''
def idf(list_pre_proc):
  '''
  :param list_pre_proc: lista dos conteúdos pré processados
  :retun: lista de tuplas com a palavra e seu valor idf calculado(list_value_idf)
  '''
def tf_idf(list_pre_proc):
  '''
  :param list_pre_proc: lista dos conteúdos pré processados
  :retun: lista de tuplas com a palavra e seu valor tfidf calculado(list_value_tfidf)
  '''
def string_tf(list_value_tfidf):
  '''
  :param list_value_tfidf:  lista de tuplas com a palavra e seu valor tfidf calculado
  :retun: retorna lista de proximidade até 2 dos 5 termos com maior tfidf(list_string_tf)
  '''
```

## 6° - Gerar um arquivo csv que possui todas as palavras de todos os documentos na primeira coluna, em que cada linha é um token. Para cada token, informe nas colunas vizinhas as informações determinadas no objetivo 5.
```
def generate_csv(list_pre_proc,list_value_tf,list_value_df,list_value_idf,list_value_tfidf):
  '''
  :param list_pre_proc: lista dos conteúdos pré processados
  :param list_value_tf: lista de tuplas com a palavra e seu valor tf calculado
  :param list_value_df: lista de tuplas com a palavra e seu valor df calculado
  :param list_value_idf: lista de tuplas com a palavra e seu valor idf calculado
  :param list_value_tfidf: lista de tuplas com a palavra e seu valor tfidf calculado
  :return: arquivo csv onde a prima coluna são todas as palavras e as colunas seguintes são seus valores (file_csv)
  '''
```

## 7° - Gerar nuvem de palavras para análise visual tal como exemplo abaixo. Cada ponto central será um dos 5 termos de maior TF-IDF. As conexões são as palavras próximas obtidas em 5.4. O tamanho do círculo da palavra é baseado no TF dela. O maior círculo que conecta o termo central será normalizado para palavras de maior TF do conjunto. (desafio)


