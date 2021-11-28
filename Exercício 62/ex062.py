print('Super Progressão Aritmética (Versão 3.0)')
print('')
print('Gerador de PA')
print('-=-' * 10)
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total += + mais
    while cont <= total:
            print('{} -> '.format(termo), end='')
            termo = termo + razão
            cont += 1
    print('Pausa.')
    print('')
    mais = int(input('Quantos termos a mais você quer adicionar? Digite aqui: '))
print('')
print('A progressão chegou ao fim. Ao todo, foram {} termos registrados.'.format(total))
