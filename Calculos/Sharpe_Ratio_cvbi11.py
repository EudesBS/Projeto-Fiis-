import pandas as pd
import numpy as np

# carrega as tabelas que vão ser usadas
df_ipca_cvbi11 = pd.read_excel("C:/Users/eudes/OneDrive/Ambiente de Trabalho/Cursos/Projeto PY/Indicadores avançados/Mensal_IPCA_FIIs_CVBI11.xlsx")
df_selic = pd.read_excel("C:/Users/eudes/OneDrive/Ambiente de Trabalho/Cursos/Projeto PY/Indicadores avançados/Semi Ratio.xlsx")

# Merge entre o bcri11 (FII) e a SELIC
df_merged = df_ipca_cvbi11[["MesAno_ComoData", "Retorno Mensal Fii"]].merge(
    df_selic[["Data", "Retorno Mensal SELIC"]],
    left_on="MesAno_ComoData", 
    right_on="Data", 
    how="left"
)


# Selecionar apenas as colunas necessárias
df_merged = df_merged[["MesAno_ComoData", "Retorno Mensal Fii", "Retorno Mensal SELIC"]]
print(df_merged)

datas_faltantes = df_ipca_cvbi11[~df_ipca_cvbi11['MesAno_ComoData'].isin(df_selic['Data'])]
print(datas_faltantes[['MesAno_ComoData']])

# Cálculo do Sharpe Ratio para cada mês
df_merged["Sharpe Ratio"] = (df_merged["Retorno Mensal Fii"] - df_merged["Retorno Mensal SELIC"]) / df_merged["Retorno Mensal Fii"].rolling(window=3).std()

# Resultado final
print(df_merged[["MesAno_ComoData", "Sharpe Ratio"]])

# Salvand o merge em formato excel
df_merged.to_excel("C:/Users/eudes/OneDrive/Ambiente de Trabalho/Cursos/Projeto PY/Indicadores avançados/Ratio_cvbi11.xlsx")