import pandas as pd

# carrega o tabelas o csv que vai ser utilizado
selic_csv = pd.read_csv("seu caminho do arquivo/Projeto PY/selic.csv")

df_selic = pd.DataFrame(selic_csv)

# Verificando cabeçalhos
print(df_selic.head(5))

# Verificando se há alguma info nula
df_selic.dropna(axis= 0, inplace= True)

# validando se há informações repetidas baseado apenas nas colunas e não no index
validar_colunas = ["Data", "Selic"]
duplicados = df_selic[df_selic.duplicated(validar_colunas)]
df_selic = df_selic.drop_duplicates(duplicados, keep= 'first')

# Salvando arquivo em excel
save_local = "seu caminho do arquivo/Projeto PY/selic.xlsx"
df_selic.to_excel(save_local, index= False, sheet_name= "Selic desde 1994")

print(df_selic.head(15))
