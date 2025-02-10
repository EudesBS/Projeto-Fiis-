import pandas as pd

# carrega as tabelas que vão ser usadas
df_ifix = pd.read_csv("seu caminho do arquivo/Projeto PY/Dados Históricos - Índice Fundos de Investimentos Imobiliários.csv")

# Verificando cabeçalhos
print(df_ifix.head(5))

# Preenchendo nulos
df_ifix.fillna('0,00k', inplace= True)

# validando se há informações repetidas baseado apenas nas colunas e não no index e deletando
colunas = ['Data', 'Último', 'Abertura', 'Máxima', 'Mínima', 'Vol.', 'Var%']
duplicados = df_ifix[df_ifix.duplicated(colunas)]
df_ifix = df_ifix.drop_duplicates(duplicados, keep= 'first')

# Arrumando o nome das colunas
df_ifix.columns= ['Data', 'Ultimo', 'Abertura', 'Maxima', 'Minima', 'Volume', 'Var%']
df_ifix.to_excel("seu caminho do arquivo/Projeto PY/dados ifix.xlsx", sheet_name= "ifix", index= False)
