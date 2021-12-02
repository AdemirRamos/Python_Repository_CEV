print('Jogo da Adivinhação (Versão 1.0)')
print()
from random import randint
from time import sleep
computador = randint (0, 5) #Faz o computador "pensar" em um número.
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
print()
jogador = int(input('Em que número eu pensei?')) #Jogador tenta adivinhar.
print('Processando...')
sleep(3)
if jogador == computador:
    print('Parabéns! Você conseguiu me vencer!')
else:
    print('Ganhei! Eu pensei no número {} e não no {}.'.format(computador, jogador))
