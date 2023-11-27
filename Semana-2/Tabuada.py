# Tabuada

# Apresentação
print('\n\t\t\t --- Cálculo da tabuada ---\n')

# Entrada
numero = int(input("Qual tabuada gostaria de calcular?: "))

# Processamento e Saída
print(f'A tabuada do {numero} é: ')

for i in range(1, 11):
    calculo = i * numero
    print(f'{numero} x {i} = {calculo}')
