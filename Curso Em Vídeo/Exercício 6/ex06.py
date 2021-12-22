print('Dobro, Triplo, Raiz Quadrada')
print()

import math

n = int(input('Digite um número: '))
print(f'\nO valor digitado foi: {n}. O dobro desse valor é: {n * 2}; o triplo desse valor é: {n * 3};', end=' ')
print(f'a raiz quadrada desse valor é: {math.sqrt(n):.2f}.')

#Resolução do Guanabara:
#Os cálculos podem ser feitos dentro de "format":
#A raiz quadrada ainda pode ser calculada de outra forma:

n = int(input('\nDigite um número: '))
d = n * 2
t = n * 3
r = n ** (1/2)
print('\nO dobro de {} vale {}.'.format(n, d)) #.format((n * 2))
print('O triplo de {} vale {}.'.format(n, t)) #.format((n * 3))
print('A raiz quadrada de {} é igual a {:.2f}.'.format(n, r)) #.format((n ** (1/2))) / #.format(pow(n, (1/2)))
