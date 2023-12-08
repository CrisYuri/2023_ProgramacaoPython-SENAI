# Calculadora Imposto de Renda v.2 - até abril/2023
# Apresentação
print('\n\t\t\t --- Calculadora de Imposto de Renda ---\n')


# Entrada

versaoCalculo = input('Deseja utilizar a versão de cáculo após Maio de 2023? (sim ou não) ')

salBruto = float(input('Salário bruto R$: '))
dependentes = int(input('Dependentes: '))
idade = int(input('Qual sua idade?: '))

# Processamento
descDependente = dependentes * 189.59
descontoSimplificado = 528.00

# Encontrar salário base
salBase = salBruto - descDependente

# Faixas de IR
faixaIsento = 1903.99
faixa1 = 2826.66
faixa2 = 3751.06
faixa3 = 4664.68

# Dedução por faixa
deducaoIsento = 0
deducao1 = 142.80
deducao2 = 354.80
deducao3 = 636.13
deducao4 = 869.36

if versaoCalculo.lower() == "sim":
    # Encontrar salário base
    if descDependente > descontoSimplificado:
        salBase = salBruto - descDependente
    else:
        salBase = salBruto - descontoSimplificado

    # Faixas de IR
    if idade > 65:
        faixaIsento = 1903.99
    else:
        faixaIsento = 2112
        faixa1 = 2826.65
        faixa2 = 3751.05
        faixa3 = 4664.68
    
    # Dedução por faixa
    deducaoIsento = 0
    deducao1 = 158.40
    deducao2 = 370.40
    deducao3 = 651.73
    deducao4 = 884.96
else:
    print('Versão incorreta')

## Encontrar faixa de IR, dedução pela faixa do salário base
if salBase < faixaIsento:
    faixa = 0
    aliq = '0%'
    deducao = deducaoIsento
elif salBase < faixa1:
    faixa = 0.075
    aliq = '7.5%'
    deducao = deducao1
elif salBase < faixa2:
    faixa = 0.15
    aliq = '15%'
    deducao = deducao2
elif salBase < faixa3:
    faixa = 0.225
    aliq = '22.5%'
    deducao = deducao3
elif salBase >= faixa3:
    faixa = 0.275
    aliq = '27.5%'
    deducao = deducao4

## Calcular o imposto bruto, IR devido, alíquota efetiva e salário líquido
irBruto = salBase * faixa
irDevido = irBruto - deducao
aliqEfetiva = irDevido / salBruto
salLiq = salBruto - irDevido

# Saída
print('\n\t --- Resultado do cálcudo do seu Imposto de Renda --- \n')
print(f'Salário bruto: R$ {salBruto:.2f}')
print(f'Dependentes: {dependentes}')
print(f'Salário base: R$ {salBase:.2f}')
if faixa != 0:
    print(f'Alíquota: {aliq}')
    print(f'Imposto devido: R$ {irDevido:.2f}') 
else:
    print('Alíquota: Isento')
    print('Alíquota: Isento')
print(f'Salário líquido: R$ {salLiq:.2f}')
if faixa != 0:
    print(f'Alíquota efetiva: {(aliqEfetiva * 100):.2f}%')
else:
    print('Alíquota: Isento')
