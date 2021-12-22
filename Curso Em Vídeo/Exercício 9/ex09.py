print('Tabuada')
print()

número = int(input('Digite um número para ver a sua tabuada: '))
print(f'\nGerando a tabuada do {número}.')
print('~' * 12)
for c in range(0, 11):
    print(f'{número} x {c} = {número * c}')
print('~' * 12)
