# Projeto para consultar a cotação de uma moeda estrangeira a partir da sigla

import requests

def getCotacao(codMoeda):
    try:
        requisicao = requests.get(f'http://economia.awesomeapi.com.br/json/last/{codMoeda}-BRL')

        # retorna requisicao.json()
        requisicao_dic = requisicao.json()

        # Retorna a cotação da moeda
        cotacao = requisicao_dic[f'{codMoeda}BRL']['bid']
        return cotacao
    except:
        print('Código da moeda inválido!')
        return None

# Teste
# Cotação da Libra Esterlina
print(f'Valor da Libra Esterlina: R$ {getCotacao("GBP")}')

# Cotação do Dolar Americano
print(f'Valor do Dólar Americano: R$ {getCotacao("USD")}')

# Cotação do Dolar Americano
print(f'Valor do Euro: R$ {getCotacao("EUR")}')