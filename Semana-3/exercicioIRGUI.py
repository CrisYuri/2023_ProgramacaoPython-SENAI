import PySimpleGUI as psg
from calcIR import*

layout = [[psg.Check('Cálculo  do IR com regra a partir de maio de 2023?', key='regra')],
          [psg.Text('Salário bruto: '), psg.InputText(key='salBruto')],
          [psg.Text('Dependentes: '), psg.InputText(key='dependentes')],
          [psg.Text('Idade: '), psg.InputText(key='idade')],
          [psg.Button('Calcular'), psg.Button('Limpar')],
          [psg.Text('--- Resultado do cálculo do seu Imposto de Renda ---')],
          [psg.Text('', key='salBase')],
          [psg.Text('', key='aliq')],
          [psg.Text('', key='irDevido')],
          [psg.Text('', key='salLiq')],
          [psg.Text('', key='aliqEfetiva')]
         ]

janela = psg.Window('Calculadora de Imposto de Renda', layout)

while True:
    evento, valores = janela.read()
    if valores['regra'] == True:
        versaoCalculo = 'sim'
    else:
        versaoCalculo = 'não'
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
        janela['regra'].update(False)
    # elif valores['v2'] == True:
    #     versaoCalculo = 'sim'
    #     salBruto = valores['salBruto']
    #     dependentes = int(valores['dependentes'])
    #     idade = int(valores['idade'])

    else:
        salBruto = float(valores['salBruto'])
        dependentes = int(valores['dependentes'])
        idade = int(valores['idade'])
        impostoRenda = calcIR(float(valores['salBruto']), int(valores['dependentes']), int(valores['idade']), str('versaoCalculo'))
        janela['salBase'].update(f"Salário base: R$ {impostoRenda['salBase']:.2f}")
        janela['aliq'].update(f"Alíquota da faixa: {impostoRenda['aliq']}")
        janela['irDevido'].update(f"IR devido: R$ {impostoRenda['irDevido']:.2f}")
        janela['salLiq'].update(f"Salário líquido: R$ {impostoRenda['salLiq']:.2f}")
        janela['aliqEfetiva'].update(f"Alíquota efetiva: {impostoRenda['aliqEfetiva']*100:.2f}%")
