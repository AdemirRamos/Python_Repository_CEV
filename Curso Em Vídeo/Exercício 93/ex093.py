print('Cadastro de Jogador de Futebol')
print()
jogador = dict()
partidas = list()
jogador['nome'] = str(input('Nome do (a) jogador (a): '))
total = int(input(f'Quantas partidas o (a) jogador (a) {jogador["nome"]} jogou? '))
print()
for c in range(1, total + 1):
    partidas.append(int(input(f'Quantos gols fez o (a) jogador (a) na {c}ª partida? ')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print('-=' * 30)
print(jogador)
print('-=' * 30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}.')
print('-=' * 30)
print(f'O (A) jogador (a) {jogador["nome"]} jogou um total de {len(jogador["gols"])} partidas.')
for i, v in enumerate(jogador['gols']):
    print(f' Na {i+1}ª partida, o (a) jogador (a) marcou {v} gol (s).')
print(f'Ao todo, o (a) jogador (a) {jogador["nome"]} marcou um total de {jogador["total"]} gol (s).')
