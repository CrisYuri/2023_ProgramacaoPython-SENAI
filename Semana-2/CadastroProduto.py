# Sistema para cadastro de produtos

estoque = []
cadastrarNovo = input('Cadastrar novo produto? (sim ou não): ')

while cadastrarNovo == 'sim':
    nomeProduto = input('Nome do produto: ')
    preco = float(input('Preço R$: '))
    quantidade = int(input('Quantidade: '))
    disponivel = input('Disponível para venda? (sim ou não): ')

    produto = {
        'nomeProduto': nomeProduto,
        'preco': preco,
        'quantidade': quantidade,
        'disponibilidade': disponivel
    }

    estoque.append(produto)

    cadastrarNovo = input('Deseja cadastrar novo produto? (sim ou não): ')

print('\n\t\t\t Catálogo de produtos \n==============================================\n')

for produto in estoque:
    print(f'Produto    | {produto['nomeProduto']}')
    print(f'Preço      | R$ {produto['preco']:.2f}')

    if produto['quantidade'] == 0:
        print('Produto indisponível no estoque')
    elif produto['disponibilidade'] == 'não':
        print(f'Quantidade | {produto['quantidade']}')
        print('Produto indisponível para venda')
        print(f'O valor total de {produto['nomeProduto']} em estoque é R$ {(produto['quantidade'] * produto['preco']):.2f} ')
    else:
        print(f'Quantidade | {produto['quantidade']}')
        print(f'Disponível | {produto['disponibilidade']}')
        print(f'O valor total de {produto['nomeProduto']} em estoque é R$ {(produto['quantidade']*produto['preco']):.2f} ')

    print('\n==============================================\n')

consultarProduto = input('Deseja consultar valor de produto em estoque? (sim ou não): ')

while consultarProduto == 'sim':
    consulta = input('Qual produto deseja consultar?: ')

    if consulta in produto['nomeProduto']:
        print(f'O valor total de {produto['nomeProduto']} em estoque é R$ {(produto['quantidade'] * produto['preco']):.2f} ')
    else:
        print('Produto indisponível no estoque')

    consultarProduto = input('Deseja consultar produto? (sim ou não): ')

print('<< fim >>')