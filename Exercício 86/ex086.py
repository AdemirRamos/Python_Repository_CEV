print('Matriz em Python')
print()
matriz = [[], [], []]
valor_1 = int(input('Digite um valor para a posição [0, 0]: '))
valor_2 = int(input('Digite um valor para a posição [0, 1]: '))
valor_3 = int(input('Digite um valor para a posição [0, 2]: '))
valor_4 = int(input('Digite um valor para a posição [1, 0]: '))
valor_5 = int(input('Digite um valor para a posição [1, 1]: '))
valor_6 = int(input('Digite um valor para a posição [1, 2]: '))
valor_7 = int(input('Digite um valor para a posição [2, 0]: '))
valor_8 = int(input('Digite um valor para a posição [2, 1]: '))
valor_9 = int(input('Digite um valor para a posição [2, 2]: '))

matriz[0].append(valor_1)
matriz[0].append(valor_2)
matriz[0].append(valor_3)
print(f'{[matriz[0][0]]}', end='')
print(f'{[matriz[0][1]]}', end='')
print(f'{[matriz[0][2]]}')
matriz[1].append(valor_4)
matriz[1].append(valor_5)
matriz[1].append(valor_6)
print(f'{[matriz[1][0]]}', end='')
print(f'{[matriz[1][1]]}', end='')
print(f'{[matriz[1][2]]}')
matriz[2].append(valor_7)
matriz[2].append(valor_8)
matriz[2].append(valor_9)
print(f'{[matriz[2][0]]}', end='')
print(f'{[matriz[2][1]]}', end='')
print(f'{[matriz[2][2]]}')

#Resolução do Guanabara:

print('Matriz em Python')
print()
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para a posição [{l}][{c}]: '))
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print(matriz)
