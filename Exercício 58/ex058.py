print('Jogo Da Adivinhação (Versão 2.0)')
print('')
from random import randint
computador = randint (0, 10)
print('''Olá! Eu sou o seu computador!
Acabei de pensear em um número de 0 a 10. \nSerá que você consegue adivinhar em qual número eu pensei?''')
print('')
jogador = int(input('Qual é o seu palpite? Digite aqui: '))
tentativas = 0
while jogador != computador:
    if jogador < computador:
        tentativas += 1
        jogador = int(input('Mais... tente mais uma vez: '))
    elif jogador > computador:
        tentativas += 1
        jogador = int(input('Menos... tente mais uma vez: '))
    if jogador == computador:
        if tentativas > 5:
            print('Você precisou de {} tentativas para acertar. Você precisa melhorar!'.format(tentativas + 1))
        elif tentativas < 5:
            print('Você precisou de {} tentativas para acertar. Você mandou muito bem!'.format(tentativas + 1))

#A seguir, temos a maneira como o Guanabara resolveu o exercício:

from random import randint
computador = randint(0, 10)
print('''Olá! Eu sou o seu computador! Eu acabei de pensar em um número entre 0 e 10.
Será que você consegue adivinhar em qual número eu pensei?''')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é o seu palpite? Digite aqui: '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... tente outra vez!')
        elif jogador > computador:
            print('Menos... tente outra vez!')
print('Acertou com {} tentativas! Parabéns!'.format(palpites))
