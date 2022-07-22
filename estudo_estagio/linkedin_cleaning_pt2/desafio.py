# %%
import pandas as pd

df = pd.read_csv('rides.csv')
df
# %%
# Find out all the rows that have bad values
# - Missing values are not allowed
# - A plate must be a combination of at least 3 upper case letters or digits
# - Distance much be bigger than 0
# %%
#Vê os nulos
null_mask = df.isnull().any(axis=1)
df[null_mask]
# %%
#Vê as placas erradas
plate_mask = ~df['plate'].str.match(r'^[0-9A-Z]{3,}', na=False)
df[plate_mask]

# %%
#Ve as linhas em que a distancia é menor que 0
dist_mask = df['distance'] < 0
df[dist_mask]
# %%
#Retorna as linhas em que ocorrem erros
mask = null_mask | plate_mask | dist_mask
df[mask]



# %%
