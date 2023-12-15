# Teste data
from Data import Data

# Criação de instância Data
dd = int(input('Digite o dia (1 a 31): '))
mm = int(input('Digite o mês (1 a 12): '))
aaaa = int(input('Digite o ano (ex. 2023): '))

minhaData = Data(dd, mm, aaaa)

# Exibindo a data
print('\n\t\t\t -- Minha Data --\n')
print(minhaData)
