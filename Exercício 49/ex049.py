print('Tabuada (Versão 2.0)')
print('')
número = int(input('Digite um número para ver a sua tabuada: '))
for tabuada in range(1, 11):
    multiplicação = tabuada * número
    print('{} x {} = {}'.format(número, tabuada, multiplicação))
print('Fim!')

#Como o Guanabara resolveu o exercício:

num = int(input('Digite um número para ver a sua tabuada: '))
for c in range(1, 11):
    print('{} x {} = {}'.format(num, c, num * c))
