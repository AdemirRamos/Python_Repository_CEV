print('Maior e Menor Valores Em Tupla')
print()
from random import randint
números = randint (1, 10), randint (1, 10), randint (1, 10), randint (1, 10), randint (1, 10) 
print(f'Os valores sorteados foram: {números}.')
for n in números:
        print(f'{n} ', end='')
print(f'\nO maior valor sorteado foi: {max(números)}.')
print(f'O menor valor sorteado foi: {min(números)}.')
