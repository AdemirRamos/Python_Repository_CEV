print('Conversor De Bases Numéricas')
print()
num = int(input('Digite um número inteiro: '))
print()
print('''Escolha uma das bases de conversão: 

[1] Converter para binário;
[2] Converter para octal;
[3] Converter para hexadecimal.''')

print()
opção = int(input('Sua opção: '))
print('')
if opção == 1:
    print('{} convertido para binário é igual a: {}.'.format(num, bin(num)[2:]))
elif opção == 2:
    print('{} convertido para octal é igual a: {}'.format(num, oct(num)[2:]))
elif opção == 3:
    print('{} convertido para hexadecimal é igual a: {}'.format(num, hex(num)[2:]))
else:
    print('Opção Inválida. Tente novamente.')
