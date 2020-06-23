import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
import json

"""
A resposta deve conter os valores da média, mediana, moda e desvio padrão 
da pontuação de crédito para cada estado do dataset.
"""

DATA_DIR = os.path.dirname(__file__) #Para execução via prompt
DATA_DIR = os.path.abspath('.') #Para execução iterativa
df = pd.read_csv(os.path.join(DATA_DIR,'desafio1.csv'))

#Problema 1: Não reconhecimento automático de cabeçalho
df = pd.read_csv(os.path.join(DATA_DIR,'desafio1.csv'),header=0)

media = list(df.groupby('estado_residencia')['pontuacao_credito'].mean())
mediana = list(df.groupby('estado_residencia')['pontuacao_credito'].median())
desvio_padrao = list(df.groupby('estado_residencia')['pontuacao_credito'].std())
moda = list(df.groupby('estado_residencia')['pontuacao_credito'].agg(lambda x:x.value_counts().index[0]))

estados = list(df['estado_residencia'].unique())
medidas = ['media', 'mediana', 'moda', 'desvio_padrao']
dict_estado1 = {}
dict_estado2 = {}
dict_estado3 = {}

for x in range(0,len(medidas)):
    if x == 0:
        dict_estado1[medidas[x]]=media[0]
        dict_estado2[medidas[x]]=media[1]
        dict_estado3[medidas[x]]=media[2]
    if x == 1:
        dict_estado1[medidas[x]]=mediana[0]
        dict_estado2[medidas[x]]=mediana[1]
        dict_estado3[medidas[x]]=mediana[2]
    if x == 2:
        dict_estado1[medidas[x]]=moda[0]
        dict_estado2[medidas[x]]=moda[1]
        dict_estado3[medidas[x]]=moda[2]
    if x == 3:
        dict_estado1[medidas[x]]=desvio_padrao[0]
        dict_estado2[medidas[x]]=desvio_padrao[1]
        dict_estado3[medidas[x]]=desvio_padrao[2]

resposta = {}
for x in range(0,len(estados)):
    if x == 0:
        resposta[estados[x]]=dict_estado1
    if x == 1:
        resposta[estados[x]]=dict_estado2
    if x == 2:
        resposta[estados[x]]=dict_estado3

json_file = json.dumps(resposta)

with open(os.path.join(DATA_DIR,'submission.json'),'w') as writing_file:
    writing_file.write(json_file)