import pandas as pd
import requests
from io import StringIO

# Endereço da API da SELIC do BC
url_selic = "https://api.bcb.gov.br/dados/serie/bcdata.sgs.11/dados?formato=csv&dataInicial=01/01/2020&dataFinal=31/12/2024"

# Executando requisição do tipo GET
response_selic = requests.get(url_selic)

# Se o status da requisição for um sucesso
if response_selic.status_code == 200:

    # Lê o arquivo do CSV diretamente em um DataFrame Panda
    data_selic = pd.read_csv(StringIO(response_selic.text), sep = ";")

    # Altera o nome das colunas
    data_selic.rename(columns= {"data": "Data", "valor": "Selic"}, inplace= True)

    # Salva o arquivo em um CSV local
    print(f"API acessada com sucesso: {response_selic.status_code}")
    data_selic.to_csv("selic.csv", index = False, encoding = "utf-8")

else:
    print(f"Erro ao acessar a API: {response_selic.status_code}")

print(data_selic.head)