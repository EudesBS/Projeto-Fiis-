import pandas as pd
import yfinance as yf

# carrega as tabelas que vão ser usadas
tickers_ipca = yf.Tickers('VCJR11.SA KNIP11.SA HCTR11.SA CVBI11.SA RZAK11.SA')
tickers_selic = yf.Tickers('OUJP11.SA MXRF11.SA BCRI11.SA HGCR11.SA RBRR11.SA')
vet_tickers_ipca = ['VCJR11.SA', 'KNIP11.SA', 'HCTR11.SA', 'CVBI11.SA', 'RZAK11.SA']
vet_tickers_selic = ['OUJP11.SA', 'MXRF11.SA', 'BCRI11.SA', 'HGCR11.SA', 'RBRR11.SA']
algo = yf.Ticker('HCTR11.SA')


# Atribuindo o histórico dos últimos 5 anos ao data_ipca 
data_ipca= tickers_ipca.history(period='5y')

# formatando data
data_ipca.index = data_ipca.index.tz_localize(None)

# Baixando dados de histórico para tabela xlsx
data_ipca.to_excel("Projeto PY/ipca-fiis.xlsx", sheet_name="fiis ipca")

# Atribuindo o histórico dos últimos 5 anos ao data_selic
data_selic= tickers_selic.history(period='5y')

# formatando data
data_selic.index = data_ipca.index.tz_localize(None)

# Baixando dados de histórico para tabela xlsx
data_selic.to_excel("seu caminho/Projeto PY/selic-fiis.xlsx", sheet_name="fiis selic")

ipca_geral_data = []
# Laço para pegar ticker por ticker da minha lista
for ticker in tickers_ipca.tickers:
    info = (tickers_ipca.tickers[ticker].info)
    info['ticker'] = ticker
    ipca_geral_data.append(info)

# Armazena ticker em uma tabela
df_ipca_geral =  pd.DataFrame(ipca_geral_data)

# Download dados gerais do IPCA
df_ipca_geral.to_excel("seu caminho/Projeto PY/ipca info geral.xlsx", sheet_name= "Dados gerais IPCA")


selic_geral_data = []
# Laço para pegar ticker por ticker da minha lista
for ticker in tickers_selic.tickers:
    info = (tickers_selic.tickers[ticker].info)
    info['ticker'] = ticker
    selic_geral_data.append(info)

# Armazena ticker em uma tabela
df_selic_geral = pd.DataFrame(selic_geral_data)

# Download dados gerais da Selic
df_selic_geral.to_excel("seu caminho do arquivo/Projeto PY/selic info geral.xlsx", sheet_name="Dados gerais Selic")
