import pandas as pd

df_selic = pd.read_excel("seu caminho do arquivo")

# Aplicando a interpolação linear na coluna 'Retorno Mensal SELIC'
df_selic['Retorno Mensal SELIC'] = df_selic['Retorno Mensal SELIC'].interpolate(method='linear')

df_selic.to_excel("seu caminho do arquivo")
