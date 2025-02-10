import pandas as pd

df_selic = pd.read_excel("C:/Users/eudes/OneDrive/Ambiente de Trabalho/Cursos/Projeto PY/Indicadores avançados/SELIC.xlsx")

# Aplicando a interpolação linear na coluna 'Retorno Mensal SELIC'
df_selic['Retorno Mensal SELIC'] = df_selic['Retorno Mensal SELIC'].interpolate(method='linear')

df_selic.to_excel("C:/Users/eudes/OneDrive/Ambiente de Trabalho/Cursos/Projeto PY/Indicadores avançados/SELIC.xlsx")