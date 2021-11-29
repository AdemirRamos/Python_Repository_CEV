print('Palpites Para a Mega-Sena')
print('-=' * 30)
print('Jogo da Mega-Sena')
import random
jogo_mega = []
jogo = int(input('Quantos jogos você quer que eu sorteie? Digite um número: '))
print()
for c in range(0, 5):
    números = random.randint(0, 60)
    jogo_mega.insert(c, números)
for c in range(1, jogo + 1):
    print(f'O {c}ª jogo sorteado foi: {jogo_mega}')

#Fiz o exercício quase completamente (mas, no final, não consegui achar um jeito de completá-lo). Resolução do Guanabara:

print('Palpites Para a Mega-Sena')
print('-=' * 30)
print('Jogo da Mega-Sena')
from random import randint
from time import sleep
lista = list()
jogos = list()
print('-' * 50)
print('     Números Para Jogar Na Mega-Sena.     ')
print('-' * 50)
quant = int(input('Quantos jogos você quer que eu sorteie? '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('-=' * 3, f'Sorteando {quant} jogos.', '-=' * 3)
print('Os números sorteado foram: {jogos}.')
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}.')
    sleep(1)
print('-=' * 5, 'Boa Sorte!', '-=' * 5)
