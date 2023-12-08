print('Para saber o signo do zodíaco, digite sua data de nascimento')

dia = int(input('Digite o dia (ex.: 25): '))
mes = input('Digite o mês (ex.: janeiro): ')

if (mes.lower() == 'dezembro' and dia >= 22) or (mes.lower() == 'janeiro' and dia <= 19):
    signo = 'Capricórnio'
elif (mes.lower() == 'janeiro' and dia >= 20) or (mes.lower() == 'fevereiro' and dia <= 18):
    signo = 'Aquário'
elif (mes.lower() == 'fevereiro' and dia >= 19) or (mes.lower() == 'março' and dia <= 20):
    signo = 'Peixes'
elif (mes.lower() == 'março' and dia >= 21) or (mes.lower() == 'abril' and dia <= 19):
    signo = 'Áries'
elif (mes.lower() == 'abril' and dia >= 20) or (mes.lower() == 'maio' and dia <= 20):
    signo = 'Touro'
elif (mes.lower() == 'maio' and dia >= 21) or (mes.lower() == 'junho' and dia <= 20):
    signo = 'Gêmeos'
elif (mes.lower() == 'junho' and dia >= 21) or (mes.lower() == 'julho' and dia <= 22):
    signo = 'Câncer'
elif (mes.lower() == 'julho' and dia >= 23) or (mes.lower() == 'agosto' and dia <= 22):
    signo = 'Leão'
elif (mes.lower() == 'agosto' and dia >= 23) or (mes.lower() == 'setembro' and dia <= 22):
    signo = 'Virgem'
elif (mes.lower() == 'setembro' and dia >= 23) or (mes.lower() == 'outubro' and dia <= 22):
    signo = 'Libra'
elif (mes.lower() == 'outubro' and dia >= 23) or (mes.lower() == 'novembro' and dia <= 21):
    signo = 'Escorpião'
else:
    signo = 'Sagitário'

print(f'Seu signo do zodíaco é {signo}')
