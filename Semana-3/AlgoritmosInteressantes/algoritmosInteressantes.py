# Tabuada
def tabuada(x):
    tabuada = []
    for i in range(1, 11):
        tabuada.append(str(x) + ' x ' + str(i) + ' = ' + str(x*i))
    return tabuada

print(tabuada(7))

# Média usando *args
def media2(*args):
    soma = 0
    for i in args:
        soma += i
    return soma/len(args)

print('A média é {:.02f}'.format(media2(4, 5, 6, 7, 8)))

# Fatorial
def fatorial(n):
    fat = 1
    for i in range(1, n+1):
        fat *= i
    return fat

print(fatorial(5))

# Fatorial com recursividade
def fat_recursivo(n):
    if n> 1:
        fat = n * fat_recursivo(n-1)
        return fat
    else:
        return 1
    
print(fat_recursivo(5))
    
#  Validador de CPF
def validadorCPF(cpf):
    # variáveis
    soma = 0
    cont = 10
    dv = 0

    if (len(cpf) == 11):
        for i in range(0,9):
            soma += int(cpf[i]) * cont
            cont -= 1

        resto = soma % 11

        if resto >= 2:
            dv = 11 - resto
        else:
            dv = 0
        
        if int(cpf[9]) == dv:

            # reinicialização das variáveis
            cont = 11
            soma = 0

            for i in range(0, 10):
                soma += int(cpf[i]) * cont
                cont -= 1
            resto = soma % 11

            if resto >= 2:
                dv = 11 - resto
            else: 
                dv = 0

            if int(cpf[10]) == dv:
                return True
            else:
                return False
        else:
            return False
    else:
        return False
    

# Teste Validador de CPF
print('CPF válido!') if validadorCPF('54647142949') else print('CPF inválido!')
print('CPF válido!') if validadorCPF('54747142949') else print('CPF inválido!')
print('CPF válido!') if validadorCPF('17824630706') else print('CPF inválido!')
print('CPF válido!') if validadorCPF('17824630806') else print('CPF inválido!')

    