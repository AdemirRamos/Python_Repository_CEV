print('Aprimorando os Dicionários')
print()
time = list()
jogador = dict()
partidas = list()
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do (a) jogador (a): '))
    total = int(input(f'Quantas partidas o (a) jogador (a) {jogador["nome"]} jogou? '))
    partidas.clear()
    print()
    for c in range(1, total + 1):
        partidas.append(int(input(f'Quantos gols fez o (a) jogador (a) na {c}ª partida? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resposta = str(input('Quer continuar? [S/N]: ')).strip().lower()[0]
        if resposta in 'sn':
            break
        print('Erro: opção digitada inválida. Responda "sim" ou "não".')
    if resposta == 'n':
        break
print('-=' * 30)
print('Cógido: ', end='')
for i in jogador.keys():
    print(f'{i:<15} ', end='')
print()
print('-' * 40)
for k, v in enumerate(time):
    print(f'{k+1:^3} ', end='')
    for d in v.values():
        print(f'{str(d):<15} ', end='')
    print()
print('-' * 40)
while True:
    busca = int(input('De qual jogador (a) você desejar ver os dados? [Selecione o número do (a) jogador (a)]: '))
    print('Para parar, digite "999".')
    if busca == 999:
        break
    if busca >= len(time):
        print('Erro. Valor digitado inválido. Selecione o número de algum jogador presente na lista.')
    else:
        print(f' -- Levantamento do jogador {time[busca]["nome"]}: ')
        for i, g in enumerate(time[busca]['gols']):
            print(f' -- No {i}ª jogo, o (a) jogador (a) marcou {g} gols.')
    print('-' * 40)
print('Fim do programa.')
