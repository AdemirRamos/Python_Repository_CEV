print('Antecessor e Sucessor')
print()

n = int(input('Digite um valor: '))
antecessor = n - 1
sucessor = n + 1
print(f'\nO número digitado foi: {n}. O antecessor desse número é: {antecessor}; o sucessor desse número é: {sucessor}.')
print(f'O número digitado foi: {n}. O antecessor desse número é: {n - 1};', end=' ')
print(f'o sucessor desse número é: {n + 1}.')
print('O número digitado foi: {}. O antecessor desse número é: {}; o sucessor desse número é: {}.'.format(n, (n - 1), (n + 1)))

#Quanto menos variáveis, mais espaço será poupado no seu programa.
