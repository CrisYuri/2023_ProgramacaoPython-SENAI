import PySimpleGUI as psg
import MySqlConexao as msqlc

layout = [[psg.Text('--- Lista de Estudantes Matriculados ---')],
          [psg.Text('Matrícula: '), psg.InputText(key='matricula')],
          [psg.Text('Nome: '), psg.InputText(key='nome')],
          [psg.Button('Ver lista'), psg.Button('Cadastrar aluno')],
          [psg.Button('Remover aluno'), psg.Button('Editar aluno')],
          [psg.Text('', key='lista')],
          [psg.Button('Limpar')]
          ]

janela = psg.Window('Lista de Estudantes Matriculados', layout)

while True:
    evento, valor = janela.read()
    if evento == psg.WIN_CLOSED:
        break
    elif evento == 'Limpar':
        janela['matricula'].update('')
        janela['nome'].update('')
        janela['lista'].update('')
    elif evento == 'Ver Lista':
        janela['lista'].update(msqlc.read(msqlc.conectar()))
    elif evento == 'Cadastrar aluno':
        m = valor['matricula']
        n = valor['nome']
        msqlc.create(msqlc.conectar(),[(m, n)])
        janela['lista'].update(msqlc.read(msqlc.conectar()))
    elif evento == 'Remover aluno':
        m = valor['matricula']
        n = valor['nome']
        msqlc.delete(msqlc.conectar(), [(m,n)])
        janela['lista'].update(msqlc.read(msqlc.conectar()))
    elif evento == 'Editar aluno':
        m = valor['matricula']
        n = valor['nome']
        msqlc.update(msqlc.conectar(),[(m, n)])
        janela['lista'].update(msqlc.read(msqlc.conectar()))

janela.close()
