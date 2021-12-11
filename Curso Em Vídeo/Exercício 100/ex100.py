print('Função Para Sortear e Somar Números (Pares)')
print()
import random
lista = list()
lista_2 = list()
contador = 0
quantidade = random.randint(1, 10)
print(f'Sorteando {quantidade} valores para a lista: ', end='')
for c in range(contador, quantidade):
    quantidade = random.randint(1, 10)
    lista.append(quantidade)
    lista.clear
print(lista, end=' ')

#Resolução do Guanabara:

print('Função Para Sortear e Somar Números (Pares)')
print()

from random import randint
from time import sleep

def sorteio(lista):
    print('Sorteando 5 valores da lista...', end=' ')
    for cont in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n}', end=' ', flush = True)
        sleep(0.3)
    print('Pronto!')

def soma_par(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores pares da lista "{lista}", temos a seguinte soma: {soma}.')

números = list()
sorteio(números)
soma_par(números)
