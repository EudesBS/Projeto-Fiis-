import pandas as pd

# carrega as tabelas que vão ser usadas
ipca_fiis = pd.read_excel('seu caminho do arquivo/Projeto PY/ipca-fiis.xlsx')
selic_fiis = pd.read_excel('seu caminho do arquivo/Projeto PY/selic-fiis.xlsx')

# convertendo todas as colunas para string
ipca_fiis =ipca_fiis.astype(str)
selic_fiis = selic_fiis.astype(str)

# verificando tipo
print(ipca_fiis['Price'].unique())

# Salvando dados
ipca_fiis.to_excel('seu caminho do arquivo/Projeto PY/ipca fiis.xlsx', sheet_name='teste')
selic_fiis.to_excel('seu caminho do arquivo/Projeto PY/selic fiis.xlsx', sheet_name='teste')
