#processamento dos dados 

#Importação das bibliotecas necessárias
import pandas as pd
import numpy as np
import re

data = pd.read_csv('netflix_titles.csv')


data = data[['title', 'listed_in', 'description']].dropna()


data['content'] = data['listed_in'] + " " + data['description']

#Normalizar os textos em 'content'
#Converter para letras minúsculas
#Remover pontuações e caracteres especiais
data['content'] = data['content'].str.lower()
data['content'] = data['content'].apply(lambda x: re.sub(r'[^\w\s]', '', x))


data.to_csv('netflix_processed.csv', index=False)
