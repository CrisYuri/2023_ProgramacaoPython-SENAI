# Calculadora simples otimizada

def soma(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mult(n1, n2):
    return n1 * n2

def div(n1, n2):
    try:
        return n1 / n2
    except ZeroDivisionError:
        print("Erro: Divisão por zero!")


#  Teste
# print(f'{2} + {2} = {soma(2, 2)}')
# print(f'{2} - {2} = {sub(2, 2)}')
# print(f'{2} * {2} = {mult(2, 2)}')
# print(f'{2} / {2} = {div(2, 2)}')

