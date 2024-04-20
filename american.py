# %%

import pandas as pd
pd.set_option('display.max_columns', None)

# %%
# Obtenção dos dados online e salvando no ambiente de trabalho 
""" # %%
url = 'https://raw.githubusercontent.com/fivethirtyeight/data/master/non-voters/nonvoters_data.csv'
df = pd.read_csv(url)
df.drop(columns='Unnamed: 0', inplace= True)
df.drop(['weight', 'RespId'], axis = 1, inplace= True)

df.to_csv('dados.csv')

"""
# %%

df = pd.read_csv('dados.csv', index_col= 'Id')

# %%
df.describe()
# %%


df.head(2)

# %%
df.shape
# Logo trabalharemos com 5800+ instâncias e 117 features.
# %%

