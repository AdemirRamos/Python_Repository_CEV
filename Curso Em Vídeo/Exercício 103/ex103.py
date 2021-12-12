print('Ficha do Jogador')
print()
def jogador(nome, gols):
    nome = 'desconhecido'
    gols = 0
    print(f'O jogador {nome} marcou {gols} gol (s).')
nome = str(input('Digite o nome do jogador: '))
gols = str(input('Digite o número de gols marcados pelo jogador: '))
jogador(nome, gols)

#Resolução do Guanabara:

print('Ficha do Jogador')
print()

def ficha(jogador = '"desconhecido"', gols = 0):
    print(f'O jogador {jogador} fez {gols} gol (s) no campeonato.')
    
    
n = str(input('Nome do jogador: '))
g = str(input('Número de gols: '))

if g.isnumeric():
    g = int(g) #Transforma o "g str" em um "g int".
else:
    g = 0

if n.strip() == '':
    ficha(gols = g)
else:
    ficha(n, g)
