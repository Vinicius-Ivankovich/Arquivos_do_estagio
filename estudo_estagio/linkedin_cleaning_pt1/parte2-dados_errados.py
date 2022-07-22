# %%
import pandas as pd

# %%
df = pd.read_csv('metrics.csv', parse_dates=['time'])
df.sample(10)

# %%
#Agrupa os dados pelo nome
df.groupby('name').describe()

# %%
#Conta as vezes que os nomes apareceram
df['name'].value_counts()

# %%
#plota um grafico com os valores dos tres nomes
pd.pivot(df, index='time', columns='name').plot(subplots=True)

# %%
#identifica valores provavelmente errados 
df.query('name == "cpu" & (value < 0 | value > 100)')

# %% 
#calcula o z score para identificar dados ruins
mem = df[df['name'] == 'mem']['value']
z_score = (mem - mem.mean())/mem.std()
bad_mem = mem[z_score.abs() > 2]
# bad_mem
df.loc[bad_mem.index]
# %%
 