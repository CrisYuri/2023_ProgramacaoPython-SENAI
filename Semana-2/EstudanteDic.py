# Estudantes | Dicionário

# Entrada e armazenamento
alunos = []

novoAluno = input('Deseja cadastrar novo aluno? (sim ou não): ')

while novoAluno == 'sim':
    nome = input('Qual o nome do aluno: ')
    matricula = input(f'{nome} está regularmente matriculado? (sim ou não): ')
    curso = input(f'Em qual curso que {nome} está matriculado?: ')
    nota = float(input(f'Qual a nota de {nome}: '))

    if nota >= 5:
        aprovacao = True
    else:
        aprovacao = False

    estudante = {
        'nome': nome,
        'matricula': matricula,
        'curso': curso,
        'nota': nota,
        'aprovacao': aprovacao
    }

    alunos.append(estudante)

    novoAluno = input('Deseja cadastrar novo aluno? (sim ou não): ')

print("\n \t\t\t\t\t Alunos Cadastrados \n =========================================================")
# Saida
for estudante in alunos:

    print(f'>>> Aluno: {estudante['nome']}')

    if estudante['matricula'] == 'sim':
        pass
    else:
        print(' ** Aluno com matrícula irregular! **')

    print(f'>>> Curso: {estudante['curso']}')
    print(f'>>> Nota: {estudante['nota']}')

    if estudante['aprovacao'] == True:
        print('>>> Aluno APROVADO!')
    else:
        print(' ** Aluno de exame! **')

    print("=========================================================")
