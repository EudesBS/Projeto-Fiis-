import pandas as pd

# carrega as tabelas que vão ser usadas
ipca_csv = pd.read_csv("C:/Users/eudes/OneDrive/Ambiente de Trabalho/Cursos/Projeto PY/ipca.csv")

df_ipca = pd.DataFrame(ipca_csv)

# Verificando cabeçalhos
print(df_ipca.head(5))

# deletando nulls 
df_ipca.dropna(axis= 0, inplace= True)

# validando se há informações repetidas baseado apenas nas colunas e não no index e deletando
colunas = ["Data", "IPCA"]
duplicados = df_ipca[df_ipca.duplicated(colunas)]
df_ipca = df_ipca.drop_duplicates(duplicados, keep= 'first')

# Salvando arquivo em excel
save_local = "C:/Users/eudes/OneDrive/Ambiente de Trabalho/Cursos/Projeto PY/ipca.xlsx"
df_ipca.to_excel(save_local, index= False, sheet_name= "IPCA desde 1994")

print(df_ipca.head(15))