# Calculadora Imposto de Renda v.2 - até abril/2023
from calcIR import*

# Apresentação

print('\n\t\t\t --- Calculadora de Imposto de Renda ---\n')


# Entrada

versaoCalculo = input('Deseja utilizar a versão de cáculo após Maio de 2023? (sim ou não) ')
salBruto = float(input('Salário bruto R$: '))
dependentes = int(input('Dependentes: '))
idade = int(input('Qual sua idade?: '))

# Processamento

calcIR(salBruto, dependentes, idade, versaoCalculo)

