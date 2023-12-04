'''
Objetivo:
- Praticar o uso e implementação de funções;
- Noção do uso de laços de repetição;
- Introdução ao uso de GUI
- Compreender o uso do import para projetos de mais de um arquivo
Proposta:- Criar um sistema de informação que converta ºC (graus celsius) em ºF (graus fahrenheit) e vice e versa;
- Leve em conta as formulas dadas;
- Use versionamento e colaboração e explore o Git e o github

C -> F = (0 °C * 9/5) + 32 = 32 °F
F -> C = (0 °F - 32) * 5/9 = -17,78 °C
'''

import PySimpleGUI as psg

# Definindo as funcões:

def calc_C_F (v1):
    return (v1 * (9 / 5)) + 32
    

def calc_F_C (v2):
    return (v2 - 32) * (5 / 9)
    


# Testes:

# print(calc_C_F(0))
# print(calc_F_C(32))


# Implementando PySimpleGUI:

layout = [
    [psg.Text('Informe a temperatura em graus Celsius: '), psg.Input(key='TempC')],
    [psg.Text('A temperatura em graus Fahrenheit é: '), psg.Text('', key='Convertido'), psg.Text('ºF')],
    [psg.Button('Converter'), psg.Button('Limpar')]
]

janela = psg.Window('Conversor de Temperatura', layout)

while True:
    evento, valores = janela.read()
    if evento == psg.WIN_CLOSED:
        break
    elif evento == 'Limpar':
        janela['TempC'].update('')
        janela['Convertido'].update('')
        janela['TempC'].set_focus()
    elif evento == 'Converter':
        tempC = int(valores['TempC'])
        total = calc_C_F('tempC')
        janela['Convertido'].update(total)
    else:
        print('Deu erro')
    
janela.close()
