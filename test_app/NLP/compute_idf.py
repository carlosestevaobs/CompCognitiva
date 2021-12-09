import sys
sys.path.insert(0, '../../')

import numpy as np
from src.nlp_proc import df, idf, ordena_list

list_exemplo = [[['câncer', 'pulmão', 'doença', 'maligna', 'comum', 'todo', 'mundo', 'todo', 'novo', 'caso', 'câncer', 'câncer', 'pulmão', 'acordo', 'global', 'burden', 'of', 'disease', 'study', 'câncer', 'pulmão', 'principal', 'causa', 'mortalidade', 'câncer', 'milhõe', 'morte', 'ano', 'e', 'todo', 'tipo', 'câncer', 'apresentar', 'grande', 'taxa', 'mortalidade', 'padronizado', 'idade', 'morte', 'habitante', 'brasil', 'instituto', 'nacional', 'câncer', 'inca', 'estimou', 'número', 'novo', 'caso', 'câncer', 'qual', 'caso', 'neoplasia', 'maligna', 'primária', 'pulmão', 'câncer', 'pulmão', 'segundo', 'tipo', 'câncer', 'grande', 'incidência', 'homem', 'quarto', 'tipo', 'câncer', 'grande', 'incidência', 'homem', 'paí', 'figurar', 'maioria', 'país', 'câncer', 'pulmão', 'principal', 'causa', 'mortalidade', 'câncer', 'brasil', 'taxa', 'sobrevida', 'ano', 'padronizado', 'idade', 'paí', 'semelhante', 'taxa', 'global', 'variar', 'taxa', 'mortalidade', 'câncer', 'pulmão', 'padronizado', 'idade', 'morte', 'habitante', 'morte', 'habitante', 'homem', 'homem', 'respectivamente', 'brasil', 'mortalidade', 'aumentar', 'morte', 'habitante', 'morte', 'habitante', 'homem', 'morte', 'habitante', 'morte', 'habitante', 'homem', 'taxa', 'mortalidade', 'tanto', 'bruto', 'ajustado', 'idade', 'homem', 'homem', 'diferiram', 'magnitude', 'todo', 'período', 'aumento', 'relativo', 'significativo', 'homem', 'homem', 'v', 'provavelmente', 'virtude', 'diferença', 'prevalência', 'tabagismo', 'figurar', 'além', 'de', 'isso', 'taxa', 'mortalidade', 'idade', 'aumentar', 'homem', 'idade', 'igual', 'superior', 'ano', 'homem', 'todo', 'idade', 'sistema', 'saúde', 'brasileiro', 'dividir', 'cobertura', 'privado', 'cobertura', 'público', 'respectivamente', 'discutir', 'adiante', 'presente', 'análise', 'evidente', 'discrepância', 'significativo', 'sistema', 'público', 'privado', 'tocante', 'disponibilidade', 'recurso', 'saúde', 'desfecho', 'paciente', 'tendência', 'mortalidade', 'câncer', 'pulmão', 'brasil', 'refletir', 'modelo', 'epidemiológico', 'mortalidade', 'relacionar', 'tabaco', 'uso', 'tabaco', 'aumentar', 'durante', 'décado', 'atingir', 'ponto', 'máximo', 'décado', 'forte', 'político', 'saúde', 'público', 'brasil', 'resultar', 'redução', 'consumo', 'tabaco', 'poder', 'servir', 'exemplo', 'outro', 'país', 'baixa', 'média', 'renda', 'estudo', 'conduzir', 'brasil', 'indicar', 'tanto', 'prevalência', 'tabagismo', 'morte', 'relacionar', 'diminuíram', 'aproximadamente', 'dado', 'proveniente', 'estudo', 'nacional', 'vigilância', 'telefone', 'sobre', 'fator', 'risco', 'doença', 'crônico', 'fator', 'proteção', 'contra', 'doença', 'mostraram', 'homem', 'homem', 'ano', 'idade', 'fumante', 'porcentagem', 'respectivamente', 'principal', 'componente', 'político', 'brasileiro', 'antitabaco', 'proibição', 'tabagismo', 'local', 'público', 'imposto', 'alto', 'sobre', 'produto', 'tabaco', 'alerta', 'saúde', 'rótulo', 'embalagem', 'cigarro', 'apesar', 'de', 'esse', 'diminuição', 'consumo', 'tabaco', 'pesquisa', 'nacional', 'criança', 'brasil', 'ainda', 'mostrar', 'prevalência', 'significativo', 'fumante', 'população', 'jovem', 'diversas', 'cidade', 'além', 'de', 'isso', 'doença', 'relacionar', 'tabagismo', 'continuar', 'ser', 'grande', 'fardo', 'saúde', 'econômico', 'estimase', 'que', 'fração', 'atribuível', 'população', 'carga', 'câncer', 'pulmão', 'relacionar', 'tabagismo', 'brasil', 'homem', 'homem', 'dado', 'relevante', 'reforçar', 'papel', 'controlo', 'local', 'tabagismo', 'dado', 'respeito', 'prevalência', 'câncer', 'pulmão', 'relacionar', 'outro', 'fator', 'risco', 'tal', 'exposição', 'amianto', 'exposição', 'fumaça', 'proveniente', 'combustão', 'lenha', 'domicílio', 'exposição', 'radônio']], [['embora', 'relativamente', 'pouco', 'dado', 'brasil', 'respeito', 'câncer', 'pulmão', 'diagnosticado', 'classificar', 'publicar', 'algum', 'dado', 'último', 'ano', 'assim', 'ocorrer', 'país', 'desenvolver', 'câncer', 'pulmonar', 'célula', 'pequeno', 'cpcnp', 'brasil', 'geralmente', 'diagnosticado', 'estágio', 'avançado', 'apresentar', 'baixo', 'taxa', 'sobrevida', 'geral', 'aproximadamente', 'paciente', 'apresentar', 'doença', 'localmente', 'avançada', 'metastático', 'estágio', 'iii', 'iv', 'respectivamente', 'acordo', 'grande', 'banco', 'dado', 'caso', 'câncer', 'estado', 'paulo', 'apenas', 'paciente', 'câncer', 'pulmão', 'reger', 'sistema', 'apresentar', 'doença', 'estágio', 'i', 'porcentagem', 'contrastam', 'referente', 'período', 'semelhante', 'eua', 'reino', 'unir', 'respectivamente', 'ensaio', 'brasileiro', 'rastreamento', 'câncer', 'pulmão', 'realizar', 'fim', 'determinar', 'eficácia', 'rastreamento', 'paí', 'janeiro', 'julho', 'voluntário', 'oferecer', 'participar', 'estudo', 'cujo', 'critério', 'elegibilidade', 'mesmo', 'aplicar', 'ensaio', 'nacional', 'rastreamento', 'pulmonar', 'realizar', 'eua', 'total', 'participante', 'receber', 'diagnóstico', 'cpcnp', 'prevalência', 'maioria', 'qual', 'classificar', 'estágio', 'i', 'publicar', 'vário', 'série', 'retrospectiva', 'qual', 'relatado', 'dado', 'proveniente', 'único', 'instituição', 'respeito', 'histologia', 'estadiamento', 'desfecho', 'câncer', 'pulmão', 'curiosamente', 'presença', 'célula', 'escamoso', 'exame', 'histológico', 'parecer', 'ser', 'prevalente', 'serviço', 'público', 'saúde', 'passo', 'adenocarcinoma', 'predomino', 'instituiçõe', 'privado', 'eua', 'taxa', 'carcinoma', 'célula', 'escamoso', 'carcinoma', 'pequeno', 'célula', 'pulmão', 'cpcp', 'diminuíram', 'após', 'décado', 'taxa', 'adenocarcinoma', 'aumentar', 'período', 'todo', 'raçasetniassexo', 'importante', 'centro', 'oncológico', 'estado', 'paulo', 'analisou', 'dado', 'coletado', 'referente', 'paciente', 'câncer', 'pulmão', 'queda', 'proporção', 'cpcp', 'dois', 'período', 'diferente', 'embora', 'ocorrer', 'alteraçõe', 'significativo', 'subgrupo', 'histológico', 'cpcnp', 'entanto', 'estudo', 'epidemiológico', 'avaliado', 'dado', 'caso', 'paciente', 'diagnóstico', 'cpcnp', 'estado', 'rio', 'janeiro', 'paulo', 'observouse', 'tendência', 'grande', 'prevalência', 'adenocarcinoma', 'carcinoma', 'célula', 'escamoso', 'exame', 'histológico', 'último', 'ano', 'v']], [['dado', 'exato', 'respeito', 'número', 'procedimento', 'cirúrgico', 'realizar', 'tratar', 'paciente', 'câncer', 'pulmão', 'acordo', 'departamento', 'informático', 'sus', 'banco', 'dado', 'sistema', 'público', 'saúde', 'cobrir', 'aproximadamente', 'população', 'brasileiro', 'mediana', 'lobectomia', 'segmentectomia', 'pulmonar', 'realizar', 'anualmente', 'entanto', 'possibilidade', 'número', 'exato', 'possível', 'lobectomia', 'segmentectomia', 'ser', 'realizar', 'tratar', 'doença', 'câncer', 'pulmão', 'banco', 'dado', 'restringir', 'sistema', 'público', 'saúde', 'qualidade', 'dado', 'questionável', 'apenas', 'pequeno', 'proporção', 'paciente', 'submeter', 'cirurgia', 'intenção', 'curativo', 'dado', 'sugerem', 'aproximadamente', 'paciente', 'submeter', 'tratamento', 'cirúrgico', 'acesso', 'cirurgia', 'curativo', 'provavelmente', 'influenciar', 'diferença', 'socioeconômico', 'performance', 'status', 'comorbidade', 'idade', 'avançada', 'distribuição', 'geográfico', 'segundo', 'secretaria', 'saúde', 'estado', 'paulo', 'probabilidade', 'realização', 'cirurgia', 'pequeno', 'paciente', 'pequeno', 'escolaridade', 'atual', 'existir', 'cirurgiõe', 'torácico', 'brasil', 'concentrar', 'regiõe', 'sul', 'sudeste', 'paí', 'pesquisa', 'promovido', 'sociedade', 'brasileiro', 'cirurgia', 'torácico', 'participante', 'dizer', 'trabalhar', 'cidade', 'milhão', 'habitante', 'portanto', 'número', 'absoluto', 'cirurgiõe', 'torácico', 'adequar', 'distribuição', 'motivo', 'preocupação', 'cidade', 'tamanho', 'médio', 'regiõe', 'densamente', 'povoado', 'centro', 'norte', 'nordeste', 'brasil', 'mal', 'servido', 'tocante', 'cirurgia', 'torácico', 'cirurgia', 'torácico', 'videoassistido', 'crescendo', 'rapidamente', 'paí', 'taxa', 'mortalidade', 'dia', 'dois', 'grande', 'série', 'caso', 'cirúrgico', 'relatado', 'incluíram', 'paciente', 'submeter', 'lobectomia', 'virtude', 'câncer', 'pulmão', 'grande', 'série', 'caso', 'internacional', 'publicar', 'ano', 'revelar', 'taxa', 'mortalidade', 'pouco', 'pequeno', 'de', 'aproximadamente', 'número', 'sugerem', 'possível', 'melhorar', 'cirurgia', 'câncer', 'pulmão', 'brasil', 'esperase', 'disseminação', 'disponibilidade', 'novo', 'técnico', 'tal', 'cirurgia', 'videoassistido', 'cirurgia', 'robótico', 'acelerem', 'processo']]]
list_1, list_2, list_3 = ordena_list(list_exemplo)
list_final = list_1 + list_2 + list_3

list_df = df(list_final)
result = idf(list_df, list_final)
print(result)