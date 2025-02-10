import pandas as pd
import numpy as np

# carrega as tabelas que vão ser usadas
df_ifix_cvbi11 = pd.read_excel("seu caminho do arquivo")
df_ifix = pd.read_excel("seu caminho do arquivo")

# Merge entre o cvbi11 (FII) e o IFIX
df_merged = df_ifix_cvbi11[["MesAno_ComoData", "Retorno Mensal Fii"]].merge(
    df_ifix[["Data", "Retorno Mensal IFIX"]],
    left_on="MesAno_ComoData", 
    right_on="Data", 
    how="left"
)

# Selecionando as 3 colunas necessárias
df_merged = df_merged[["MesAno_ComoData", "Retorno Mensal Fii", "Retorno Mensal IFIX"]]

# Renomeando a coluna de data para algo mais intuitivo
df_merged = df_merged.rename(columns={"MesAno_ComoData": "Data"})

# Visualizar os primeiros resultados
print(df_merged.head(15))

# Lista para armazenar os valores de Beta por mês
betas = []

# Iterando mês a mês para calcular o Beta
for i in range(1, len(df_merged)):
    # Subconjunto de dados até o mês i
    data_subset = df_merged.iloc[:i+1]
    
    # Calculando a covariância e variância para o mês
    cov_matrix = data_subset[["Retorno Mensal Fii", "Retorno Mensal IFIX"]].cov()
    
    # Calculando o Beta
    beta = cov_matrix.iloc[0, 1] / cov_matrix.iloc[1, 1]
    
    # Adicionando o valor de Beta à lista
    betas.append(beta)

# Adicionando a coluna de Beta ao DataFrame, alinhando os valores com a Data
df_merged["Beta Mensal"] = [None] + betas  # O primeiro mês não terá Beta

# Exibindo o resultado
print(df_merged)

# Salvand o merge em formato excel
df_merged.to_excel("seu caminho do arquivo")
