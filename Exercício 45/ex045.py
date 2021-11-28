print('Jokenpô')
print('')
print('Vamos jogar', '{:=^20}'.format('Jokenpô!'))
import random
from time import sleep
print('''Suas opções são:

[1] Pedra;
[2] Papel;
[3] Tesoura.''')
lista = [1, 2, 3]
computador = random.choice(lista)
print('')
jogador = int(input('Qual opção você escolhe? '))
if jogador != 1 and jogador != 2 and jogador != 3:
    print('\033[31mOpção Inválida Tente novamente.\033[m')
else:
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PÔ!')
    sleep(1)
    print('-=-' * 25)
    if computador == 1 and jogador == 2:
        print('O computador escolheu pedra e você escolheu papel. Você venceu.')
    elif computador == 2 and jogador == 1:
        print('O computador escolheu papel e você pedra. O computador venceu.')
    elif computador == 3 and jogador == 1:
        print('O computador escolheu tesoura e você escolheu pedra. Você venceu.')
    elif computador == 1 and jogador == 3:
        print('O computador escolheu pedra e você escolheu tesoura. O computador venceu.')
    elif computador == 2 and jogador == 3:
        print('O computador escolheu papel e você tesoura. Você venceu.')
    elif computador == 3 and jogador == 2:
        print('O computador escolheu tesoura e você papel. O computador venceu. ')
    elif jogador == computador:
        print('Deu impate! Você e o computador escolheram a mesma opção.')
    print('-=-' * 25)

#A seguir temos a maneira como o Guanabara resolveu o exercício.

itens = ('pedra', 'papel', 'tesoura')
from random import randint
from time import sleep
computador = randint(0, 2)
print('''Suas opções:
[0] Pedra;
[1] Papel;
[2] Tesoura.''')
jogador = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep (1)
print('PÔ!')
sleep(1)
print('-=-' * 11)
print('computador jogou {}'.format(itens[computador]))
print('jogador jogou {}'.format(itens[computador]))
print('-=-' * 11)
if computador == 0: #computador jogou pedra.
    if jogador == 0:
        print('Empate!')
    elif jogador == 1:
        print('Jogador venceu!')
    elif jogador == 2:
        print('Computador venceu!')
    else:
        print('Jogada Inválida.')
elif computador == 1: #computador jogou papel.
    if jogador == 0:
        print('Computador venceu!')
    elif jogador == 1:
        print('Empate!')
    elif jogador == 2:
        print('Jogador venceu!')
    else:
        print('Jogada inválida.')
elif computador == 2: #computador jogou tesoura.
    if jogador == 0:
        print('Jogador venceu!')
    elif jogador == 1:
        print('Computador venceu!')
    elif jogador == 2:
        print('Empate!')
    else:
        print('Opção Inválida.')
