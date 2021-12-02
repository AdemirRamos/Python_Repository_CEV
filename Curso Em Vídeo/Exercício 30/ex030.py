print('Par ou Ímpar')
print()
número = int(input('Me diga um número qualquer: '))
resultado = número % 2
if resultado == 0:
    print('Este número ({}) é par.'.format(número))
else:
    print('Este número ({}) é ímpar.'.format(número))
