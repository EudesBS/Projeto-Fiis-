from google.cloud import bigquery
from pandas_gbq import to_gbq                    # na ausencia use, "pip install pandas-gbq" em seu terminal
from google.oauth2 import service_account        # na ausencia use, "pip install google-auth" em seu terminal
import pandas as pd

from pandas_gbq import to_gbq                    # na ausencia use, "pip install pandas-gbq" em seu terminal
from google.oauth2 import service_account        # na ausencia use, "pip install google-auth" em seu terminal
import pandas as pd

# id do projeto GoogleBigQuery
id_project = 'finance-project-449001'

# Carregando credenciais (Assim que criado uma credencial no Google BigQuerty um json é gerado automaticamente)
credencial = service_account.Credentials.from_service_account_file(
    r'C:/Users/eudes/OneDrive/Ambiente de Trabalho/Cursos/Projeto PY/finance-project-449001-132c28defe79.json',
    scopes = ['https://www.googleapis.com/auth/bigquery']
)

# Lendo DataFrames que seram enviados ao Google BigQuery (Esses DFs foram gerados na etapa de Transform)
df_ipca= pd.read_excel('C:/Users/eudes/OneDrive/Ambiente de Trabalho/Cursos/Projeto PY/ipca.xlsx')
df_selic= pd.read_excel('C:/Users/eudes/OneDrive/Ambiente de Trabalho/Cursos/Projeto PY/selic.xlsx')
df_ifix= pd.read_excel('C:/Users/eudes/OneDrive/Ambiente de Trabalho/Cursos/Projeto PY/dados ifix.xlsx')
df_ipca_fiis= pd.read_excel('C:/Users/eudes/OneDrive/Ambiente de Trabalho/Cursos/Projeto PY/ipca fiis.xlsx')
df_selic_fiis= pd.read_excel('C:/Users/eudes/OneDrive/Ambiente de Trabalho/Cursos/Projeto PY/selic fiis.xlsx')
df_selic_geral= pd.read_excel('C:/Users/eudes/OneDrive/Ambiente de Trabalho/Cursos/Projeto PY/selic info geral.xlsx')
df_ipca_geral = pd.read_excel('C:/Users/eudes/OneDrive/Ambiente de Trabalho/Cursos/Projeto PY/ipca info geral.xlsx')

# 
to_gbq(dataframe= df_ipca,
       destination_table='finance-project-449001.fiis_comportamentos.IPCA',
               project_id= id_project,
               if_exists= 'replace',
               credentials= credencial)

to_gbq(dataframe= df_selic,
        destination_table='finance-project-449001.fiis_comportamentos.SELIC',
                project_id=id_project,
                if_exists= 'replace',
                credentials=credencial)

to_gbq(dataframe=df_ifix,
       destination_table='finance-project-449001.fiis_comportamentos.IFIX',
       project_id=id_project,
       if_exists='replace',
       credentials=credencial)

to_gbq(dataframe=df_ipca_geral,
       destination_table='finance-project-449001.fiis_comportamentos.IPCA_FIIS_GERAL',
       project_id=id_project,
       if_exists='replace',
       credentials=credencial)

to_gbq(dataframe=df_selic_geral,
       destination_table='finance-project-449001.fiis_comportamentos.SELIC_FIIS_GERAL',
       project_id=id_project,
       credentials=credencial)

to_gbq(dataframe=df_ipca_fiis,
       destination_table='finance-project-449001.fiis_comportamentos.IPCA_FIIS',
       project_id=id_project,
       if_exists='replace',
       credentials=credencial)

to_gbq(dataframe=df_selic_fiis,
       destination_table='finance-project-449001.fiis_comportamentos.SELIC_FIIS',
       project_id=id_project,
       if_exists='replace',
       credentials=credencial)