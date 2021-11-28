'''for c in range(1, 10):
    print(c)
print('Fim!')'''

'''c = 1
while c < 10:
    print(c)
    c += 1 #c += 1 é igual a: c = c + 1
print('Fim!')'''

'''for c in range(1, 5):
    n = int(input('Digite um valor: '))
print('Fim!')'''

'''n = 1
while n != 0:
    n = int(input('Digite algum valor: '))
print('Você digitou zero. Acabou!')'''

'''r = 's'
while r == 's':
    n = int(input('Digite algum valor: '))
    r = str(input('Quer continuar [S/N]: ')).lower()
print('Acabou!')
print('')'''
n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite algum valor: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        elif n % 1 == 0:
            impar += 1
print('Você digitou {} números pares e {} números ímpares.'.format(par, impar))
