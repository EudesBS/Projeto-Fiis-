import requests
import pandas as pd

# Endereço API do IPCA BC
url_ipca = "https://api.bcb.gov.br/dados/serie/bcdata.sgs.10844/dados?formato=csv&dataInicial=01/01/2020&dataFinal=31/12/2024"

# Executando uma requisição
response_ipca = requests.get(url_ipca)

# verifica se a requisição foi um sucesso
if response_ipca.status_code == 200:

    # Lê o arquivo do CSV diretamente em um DataFrame Panda
    from io import StringIO
    data_ipca = pd.read_csv(StringIO(response_ipca.text), sep = ";")

    # Renomeando as colunas do arquivo e fazendo a substituição
    data_ipca.rename(columns= {"data": "Data", "valor": "IPCA"}, inplace=True)


    # Salva o DataFrame em um CSV local 
    print(f"API acessada com sucesso: {response_ipca.status_code}")
    data_ipca.to_csv("ipca.csv", index= False, encoding = "utf-8")
    
else:
    print(f"Erro ao acessar a API: {response_ipca.status_code}")