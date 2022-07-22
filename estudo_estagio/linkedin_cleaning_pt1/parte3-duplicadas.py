# %%
import pandas as pd


# %%
df = pd.read_csv('cart2.csv', parse_dates=['date'])
df
# %%
#mostra as linhas que são duplicatas
df.duplicated()

# %%
#Mostra as linhas que são duplicatasconsiderando data e nome
df.duplicated(['date', 'name'])
# %%
