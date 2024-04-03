import requests

def obter_taxas():
    url = 'https://api.exchangerate-api.com/v4/latest/USD'
    response = requests.get(url)
    data = response.json()
    return data ['rates']

def converter_moedas (valor, moeda_origem, moeda_destino, taxas):
    if moeda_origem in taxas and moeda_destino in taxas:
        taxa_origem = taxas[moeda_origem]
        taxa_destino = taxas[moeda_destino]
        valor_em_usd = valor / taxa_origem
        valor_convertido = valor_em_usd * taxa_destino

        return valor_convertido
    else:
        return None
    
taxa_de_cambio = obter_taxas()
valor = float(input('Qual valor deseja converter ?'))
moeda_origem = input('Qual é a moeda de origem ?').upper()
moeda_destino = input('Qual é a moeda que deseja converter ?').upper()

valor_convertido = converter_moedas (valor, moeda_origem, moeda_destino, taxa_de_cambio)

if valor_convertido is not None:
    print(f'\n{valor:.2f} {moeda_origem} é equivalente a {valor_convertido:.2f} {moeda_destino}')
else:
    print('Moedas não encontradas')



