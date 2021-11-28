print('Análise De Dados Em Uma Tupla')
print()
núm = int(input('Digite um número: ')), int(input('Digite outro um número: ')), int(input('Digite mais um número: ')), int(input('Digite um último número: '))
print(f'Você digitou os valores: {núm}.')
print(f'O valor 9 apareceu {núm.count(9)} vezes.')
if 3 in núm:
        print(f'O valor três apareceu na {núm.index(3) + 1}ª posição.')
else:
        print('O valor três (3) não foi digitado.')
print(f'Os valores pares (digitados) foram: ', end='')
for n in núm:
        if n % 2 == 0:
                print(n , end=' ')
