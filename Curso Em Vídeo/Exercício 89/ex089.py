print('Boletim Com Listas Compostas')
print()
ficha = list()
while True:
    nome = str(input('Nome: '))
    nota_1 = float(input('1ª Nota: '))
    nota_2 = float(input('2ª Nota: '))
    média = nota_1 + nota_2 / 2
    ficha.append([nome, [nota_1, nota_2], média])
    resposta = str(input('Quer continuar? [S/N]')).strip().lower()
    if resposta in 'n':
        break
print('-=' * 30)
print(f'{"No.":<4}{"Nome":<10}{"Média":>8}')
print('-' * 26)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-' * 35)
    opção = int(input('De qual aluno você gostaria de ver as notas? (Digite "999" para parar o programa)'))
    if opção == 999:
        print('Finalizando o programa.')
        break
    if opção <= len(ficha) - 1:
        print(f'Notas de {ficha[opção][0]} são {ficha[opção][1]}.')
print('Volte sempre!')
