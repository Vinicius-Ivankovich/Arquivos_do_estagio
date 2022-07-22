
# %%
# importa pandas e lê o csv
import pandas as pd


df = pd.read_csv('cart.csv', parse_dates=['date'])
df



# %%
#Identifica valores nulos, NaT , NaN
df.isnull()

# %%
#Retorna em quais linhas tem valores nulos, NaT , NaN
df.isnull().any(axis=1)



