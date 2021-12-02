print('Contagem De Pares')
print()
for pares in range(2, 51, 2):
    #print('.', end='') -> Essa linha de código vai mostrar quantos laços o programa fez.
    print(pares, end=' ')
print('\nEsses são os números pares.')
print('')

#Maneira como o Guanabara resolveu o exercício:

for pares in range(2, 51, 2):
    if pares % 2 == 0:
        print(pares, end=' ')
print('\nEsses são os números pares.')
