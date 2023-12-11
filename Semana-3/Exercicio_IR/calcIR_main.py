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

impostoRenda = calcIR(salBruto, dependentes, idade, versaoCalculo)

print('\n\t --- Resultado do cálcudo do seu Imposto de Renda --- \n')
print(f'Salário bruto: R$ {salBruto:.2f}')
print(f'Dependentes: {dependentes}')
print(f"Salário base: R$ {impostoRenda['salBase']:.2f}")
print(f"Alíquota da faixa: {impostoRenda['aliq']}")
print(f"IR devido: R$ {impostoRenda['irDevido']:.2f}")
print(f"Salário líquido: R$ {impostoRenda['salLiq']:.2f}")
print(f"Alíquota efetiva: {impostoRenda['aliqEfetiva']*100:.2f}%")
