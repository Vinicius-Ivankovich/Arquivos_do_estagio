# %%
import pandas as pd

df = pd.read_csv('ships.csv')
df

# %%

df[df.isnull().any(axis=1)]
# %%
#vê o ultimo nome
df.iloc[-1]['name']
# %%
#Tira os espaços em branco
df['name'] = df['name'].str.strip()
df.iloc[-1]['name']

# %%
df[df.isnull().any(axis=1)]

# %%
#transforma strings em branco em NaN do numpy
import numpy as np
mask = df['name'].str.strip() == ''
df.loc[mask, 'name'] = np.nan
# %%

df[df.isnull().any(axis=1)]
# %%
