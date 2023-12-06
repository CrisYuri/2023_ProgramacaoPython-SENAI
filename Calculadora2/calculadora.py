#  Interface da calculadora

from calc2 import*

while True:
    # Apresentação
    print('\n\t\t\t --- Calculadora Simples ---\n')

    # Menu
    print('1. Soma')
    print('2. Subtração')
    print('3. Multiplicação')
    print('4. Divisão')
    print('5. Sair')

    op = int(input('\nOpção: '))

    if op == 1:

        # Entradas
        n1 = int(input('Informe n1: '))
        n2 = int(input('Informe n2: '))

        # Processamento
        total = soma(n1, n2)

        # Saída
        print(f'{n1} + {n2} = {total}')
    
    elif op == 2:
        # Entradas
        n1 = int(input('Informe n1: '))
        n2 = int(input('Informe n2: '))

        # Processamento
        total = sub(n1, n2)

        # Saída
        print(f'{n1} - {n2} = {total}')
    
    elif op == 3:
        # Entradas
        n1 = int(input('Informe n1: '))
        n2 = int(input('Informe n2: '))

        # Processamento
        total = mult(n1, n2)

        # Saída
        print(f'{n1} * {n2} = {total}')
    
    elif op == 4:
        # Entradas
        n1 = int(input('Informe n1: '))
        n2 = int(input('Informe n2: '))

        # Processamento
        total = div(n1, n2)

        # Saída
        print(f'{n1} / {n2} = {total}')
    
    elif op == 5:
        print('\nAté logo!\n')
        break
    
    else:
        print(f'Opção {op} incorreta!')


