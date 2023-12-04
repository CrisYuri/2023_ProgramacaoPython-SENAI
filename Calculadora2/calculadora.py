#  Interface da calculadora

from calc2 import soma

#  Apresentação
print('\n\t\t\t -- Calculadora 2 --\n')

#  Entrada
num1 = int(input('Informe o n1: '))
num2 = int(input('Informe o n2: '))

#  Processamento
print(f'total = {soma(num1, num2)}')

