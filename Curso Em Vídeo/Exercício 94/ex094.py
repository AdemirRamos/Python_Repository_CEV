print('Unindo Dicionários e Listas')
print()
galera = list()
pessoa = dict()
soma = média = 0
while True:
    pessoa.clear() #Este comando vai esvaziar a lista "pessoa" toda vez que a repetição for reiniciada.
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo [M/F]: ')).strip().upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('Erro! Opção digitada inválida. Escolha entre o sexo masculino e feminino.')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:       
        resposta = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
        if resposta in 'SN':
            break
        print('Erro! Opção digitada inválida. Escolha entre "sim" ou "não".')
    if resposta == 'N':
        break
print()
print(f'A) Ao todo, temos {len(galera)} pessoas cadastradas.')
média = soma / len(galera)
print(f'B) A média de idade das pessoas cadastradas é de: {média:5.2f} anos de idade.')
print(f'C) As mulheres cadastradas foram: ', end='')
for p in galera:
    if p['sexo'] == 'F': #Esta linha também poderia ser escrita assim: "if p['sexo'] in 'Ff':".
        print(f'{p["nome"]} ', end='')
print()
print('D) Lista de pessoas com a idade acima da média: ')
for p in galera:
    if p['idade'] >= média:
        print('    ', end='')
        for k, v in p.items():
            print(f'{k}; = {v}; ', end='')
        print()
print('Fim do programa.')
