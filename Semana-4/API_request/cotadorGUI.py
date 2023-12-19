# Interface gráfica com o usuário

import PySimpleGUI as psg
from cotacao import getCotacao
layout = [
    [psg.Text('Informe o código da moeda: '), psg.Combo(['USD', 'GBP', 'EUR'], key='moeda', default_value='GBP')],
    [psg.Text('', key='resultado')],
    [psg.Button('Calcular')],
]

janela = psg.Window('Cotação de Moeda Estrangeira', layout)

while True:
    eventos, valores = janela.read()

    if eventos == psg.WIN_CLOSED:
        break
    else:
        valor = getCotacao(valores['moeda'])
        janela['resultado'].update('{} 1,00 = R$ {:.2f}'.format(valores['moeda'], float(valor)))

janela.close()