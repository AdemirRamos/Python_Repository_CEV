print('Cadastro de Trabalhador em Python')
print()
nome = input('Nome: ')
ano_nascimento = int(input('Ano de nascimento: '))
carteira_trabalho = int(input('Carteira de trabalho (0: trabalhor sem carteira): '))
if carteira_trabalho != 0:
    ano_contratação = int(input('Digite o ano de contratação do trabalhador: '))
    vencimentos = float(input('Digite o salário do trabalhador: R$'))
    dados = {'nome': nome, 'idade': 2021 - ano_nascimento, 'carteira': carteira_trabalho, 'contratação': ano_contratação, 'salário': vencimentos}
    print()
    print('Os dados coletados foram:')
    print(f'O nome do (a) funcionário (a) é: {dados["nome"]}.')
    print(f'A CTPS do (a) funcionário (a) é {dados["carteira"]}.')
    print(f'A idade do (a) funcionário (a) é: {dados["idade"]}.')
    print(f'O ano de contratação do (a) funcionário (a) é: {dados["contratação"]}.')
    print(f'O salário do (a) funcionário (a) é de: R${dados["salário"]}.')
else:
    dados = {'nome': nome, 'idade': ano_nascimento, 'carteira': carteira_trabalho}
    print()
    print('Os dados coletados foram:')
    print(f'O nome do (a) funcionário (a) é: {dados["nome"]}.')
    print(f'A CTPS do (a) funcionário é: o (a) funcionário (a) não possui CTPS.')
    print(f'A idade do (a) funcionário (a) é: {dados["idade"]}.')

#A seguir, temos a resolução do Guanabara:

from datetime import datetime
dados = dict()
dados['nome'] = str(input('Nome: '))
nascimento = int(input('Ano de Nascimento: '))
dados['idade'] = datetime.now().year - nascimento
dados['ctps'] = int(input('Cateira de Trabalho (0 para trabalhador sem Carteira de Trabalho): '))
if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de contratação: '))
    dados['salário'] = float(input('Salário: R$'))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratação'] + 35) - datetime.now().year)
print('-=' * 30)
for k, v in dados.items():
    print(f' - {k} tem o valor {v}.')
