print('Cálculo Do Fatorial')
print('')
from math import factorial
num = int(input('Digite um número para calcular o seu fatorial: '))
f = factorial(num)
print('O fatorial de {} é {}'.format(num, f))
print('')
num = int(input('Digite um número para calcular o seu fatorial: '))
c = num
f = 1
print('Calculando o {}! = '.format(num), end = '')
while c > 0:
    print('{}'.format(c), end = ' ')
    print('x ' if c > 1 else '= ', end = '')
    f = f * c #Outra digitação possível: f *= c
    c -= 1
print(f'{f}.')
