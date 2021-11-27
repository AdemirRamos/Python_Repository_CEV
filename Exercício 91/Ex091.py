print('Jogo de Dados em Python')
print()
import random
contador = 0
print('Valores Sorteados:')
for c in range(1, 5):
    print(f'{c}ª jogador tirou {random.randint(1, 6)} ao rolar o dado.')
print()
print('Ranking dos Jogadores:')
print()
for c in range(1, 5):
    print(f'{c}ª lugar: ')

#2ª:

print('Jogo de Dados em Python')
print()
import random
número_1 = random.randint(1, 6)
número_2 = random.randint(1, 6)
número_3 = random.randint(1, 6)
número_4 = random.randint(1, 6)
jogadores = {'jogador 1': número_1, 'jogador 2': número_2, 'jogador 3': número_3, 'jogador 4': número_4}
print('Valores Sorteados:')
for j in jogadores:
    print(f'{j}ª jogador tirou {jogadores[j]} ao rolar o dado.')
print()
print('Ranking dos Jogadores:')
print()
for c in range(1, 5):
    print(f'{c}ª lugar: ')

#Para solucionar a segunda parte deste exercício, será preciso um conteúdo que não foi mostrado durante a aula.
#A seguir temos a resolução do Guanabara mais esse conteúdo:

from random import randint
from time import sleep
from operator import itemgetter

jogo = {'jogador 1': randint(1, 6), 'jogador 2': randint(1, 6), 'jogador 3': randint(1, 6), 'jogador 4': randint(1, 6)}
ranking = dict() #Você pode, se assim desejar, transformar "ranking" em uma lista.
print()
print('Valores Sorteados:')
print()
for k, v in jogo.items():
    print(f'{k} tirou o valor {v} ao rolar os dados.')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print()

#Caso o valor seja 0, o resultado será mostrado em ordem de chave, no caso de 1, o resultado será mostrado em ordem de valor.
#O resultado apresentado virá no formato de lista, portanto, ao manipulá-lo, é preciso atentar-se a esse fato.

print('Ranking dos Jogadores:')
print()
for i, v in enumerate(ranking):
    print(f'No {i+1}ª lugar temos: {v[0]} com o valor "{v[1]}".')
    sleep(1)
