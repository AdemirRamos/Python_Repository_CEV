print('Listas Com Pares e Ímpares')
print()
números = [[], []]
valor = 0
for c in range(1, 8):
    número = (int(input(f'Digite o {c}ª número: ')))
    if número % 2 == 0:
        números[0].append(número)
    else:
        números[1].append(número)
números[0].sort()
números[1].sort()
print()
print(f'Os valores pares digitados foram: {números[0]}.')
print(f'Os valores ímpares digitados foram: {números[1]}.')
