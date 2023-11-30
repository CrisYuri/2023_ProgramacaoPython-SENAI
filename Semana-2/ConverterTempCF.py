'''
Objetivo:
- Praticar o uso de funções;
- Introduzir o uso de laços de repetição;
- Compreender o uso do import para projetos de mais de um arquivo
Proposta:
- Criar um sistema de informação que use menu para converter ºC (graus celsius) em ºF (graus fahrenheit) e vice e versa;
- Leve em conta as formulas dadas;
- Use versionamento e colaboração e explore o Git e o github

C -> F = (0 °C × 9/5) + 32 = 32 °F
F -> C = (0 °F − 32) × 5/9 = -17,78 °C
'''

import PySimpleGUI as sg

temperatura = float(input('Temperatura: '))
unidade = input('Unidade? (C ou F): ')

if unidade == 'C':
    tempConv = (temperatura * 9 / 5) + 32
    print(f'{temperatura:.2f}C = {tempConv:.2f}F')
elif unidade == 'F':
    tempConv = (temperatura - 32) * 5 / 9
    print(f'{temperatura:.2f}F = {tempConv:.2f}C')
