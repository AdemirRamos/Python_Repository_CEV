print('Exercício 103')
print()
def jogador(nome, gols):
    nome = 'desconhecido'
    gols = 0
    print(f'O jogador {nome} marcou {gols} gol (s).')
nome = str(input('Digite o nome do jogador: '))
gols = str(input('Digite o número de gols marcados pelo jogador: '))
jogador(nome, gols)