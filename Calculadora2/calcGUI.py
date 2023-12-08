#  Interface gráfica

import PySimpleGUI as psg

import calc2

layout = [
    [psg.Radio('Soma', 'operação', key='soma', default=True), psg.Radio('Subtração', 'operação', key='sub')],
    [psg.Radio('Multiplicação', 'operação', key='mult'), psg.Radio('Divisão', 'operação', key='div')],
    [psg.Text('Informe N1: '), psg.InputText(key='Num1')],
    [psg.Text('Informe N2: '), psg.InputText(key='Num2')],
    [psg.Text('<<<< '), psg.Text('', key='total'), psg.Text(' >>>>')],
    [psg.Button('Calcular'), psg.Button('Limpar')]
    ]

janela = psg.Window('Calculadora Simples', layout)

while True:
    evento, valores = janela.read()
    if evento == psg.WIN_CLOSED:
        break
    elif evento == 'Limpar':
        janela['Num1'].update('')
        janela['Num2'].update('')
        janela['total'].update('')
        janela['Num1'].set_focus()
    elif valores['soma'] == True:
        num1 = int(valores['Num1'])
        num2 = int(valores['Num2'])
        janela['total'].update(calc2.soma(num1, num2))
    elif valores['sub'] == True:
        num1 = int(valores['Num1'])
        num2 = int(valores['Num2']) 
        janela['total'].update(calc2.sub(num1, num2))
    elif valores['mult'] == True:
        num1 = int(valores['Num1'])
        num2 = int(valores['Num2']) 
        janela['total'].update(calc2.mult(num1, num2))
    elif valores['div'] == True:
        num1 = int(valores['Num1'])
        num2 = int(valores['Num2'])
        if num2 != 0:
            janela['total'].update(calc2.div(num1, num2))
        else:
            psg.popup('Divisão por zero!')
            janela['Num2'].update('')
            continue
        
janela.close()