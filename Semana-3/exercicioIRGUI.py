import PySimpleGUI as psg
from calcIR import*
import sys

layout = [[psg.Text('Escolha a versão de cáculo de Imposto de renda que deseja utilizar')],
          [psg.Radio('Até abril de 2023', 'versao', key='v1'), psg.Radio('Após maio de 2023', 'versao', key='v2', default=True)],
          [psg.Text('Salário bruto: '), psg.InputText(key='salBruto')],
          [psg.Text('Dependentes: '), psg.InputText(key='dependentes')],
          [psg.Text('Idade: '), psg.InputText(key='idade')],
          [psg.Button('Calcular'), psg.Button('Limpar')],
          [psg.Text('--- Resultado do cálculo do seu Imposto de Renda ---')],
          [psg.Output(size=(50, 10), key='saida')]
         ]

janela = psg.Window('Calculadora de Imposto de Renda', layout)

while True:
    evento, valores = janela.read()
    if evento == psg.WIN_CLOSED:
        break
    elif evento == 'Limpar':
        janela['salBruto'].update('')
        janela['dependentes'].update('')
        janela['idade'].update('')
        janela['salBruto'].set_focus()
        janela['salBase'].update('')
        janela['aliq'].update('')
        janela['irDevido'].update('')
        janela['salLiq'].update('')
        janela['aliqEfetiva'].update('')
    elif valores['v2'] == True:
        versaoCalculo = 'sim'
        salBruto = valores['salBruto']
        dependentes = int(valores['dependentes'])
        idade = int(valores['idade'])
        original_stdout = sys.stdout
        sys.stdout = janela['saida'].TKOut
        calcIR()
        sys.stdout = original_stdout
    else:
        versaoCalculo = 'não'
        salBruto = float(valores['salBruto'])
        dependentes = int(valores['dependentes'])
        idade = int(valores['idade'])
        original_stdout = sys.stdout
        sys.stdout = janela['saida'].TKOut
        calcIR()
        sys.stdout = original_stdout
        