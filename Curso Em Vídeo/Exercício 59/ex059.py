print('Criando Um Menu De Opções')
print('')
valor1 = int(input('Digite o primeiro valor: '))
valor2 = int(input('Digite o segundo valor: '))
print('''
[1] Somar;
[2] Multiplicar;
[3] Novos Números;
[4] Dividir;
[5] Elevar nº1 ao n2º;
[6] Elevar nº2 ao nº1;
[7] Maior Número;
[8] Sair do Programa.''')
print('')
opção = int(input('Qual opção você escolhe? '))
while opção != 8:
    if opção == 1:
        soma = valor1 + valor2
        print('A soma entre {} + {} é igual a: {}.'.format(valor1, valor2, soma))
        print('')
        print('Pressione 9 para rever as opções.')
        opção = int(input('Qual opção você escolhe? '))
    elif opção == 2:
        multi = valor1 * valor2
        print('A multiplicação de {} x {} é igual a: {}.'.format(valor1, valor2, multi))
        print('')
        print('Pressione 9 para rever as opções.')
        opção = int(input('Qual opção você escolhe? '))
    elif opção == 3:
        valor1 = int(input('Digite o 1ª novo valor: '))
        valor2 = int(input('Digite o 2ª novo valor: '))
        print('')
        print('Pressione 9 para rever as opções.')
        opção = int(input('Qual opção você escolhe? '))
    elif opção == 4:
        divi = valor1 / valor2
        print('A divisão entre {} e {} é igual a: {:.2f}.'.format(valor1, valor2, divi))
        print('')
        print('Pressione 9 para rever as opções.')
        opção = int(input('Qual opção você escolhe? '))
    elif opção == 5:
        potência1 = valor1 ** valor2
        print('O primeiro valor ({}) elevado ao segundo valor ({}) é igual a: {}.'.format(valor1, valor2, potência1))
        print('')
        print('Pressione 9 para rever as opções.')
        opção = int(input('Qual opção você escolhe? '))
    elif opção == 6:
        potência2 = valor2 ** valor1
        print('O segundo valor ({}) elevado ao primeiro valor ({}) é igual a: {}.'.format(valor2, valor1, potência2))
        print('')
        if valor1 > valor2:
            maior = valor1
            print('Entre {} e {} o maior valor é: {}.'.format(valor1, valor2, maior))
            print('')
        elif valor2 > valor1:
            maior = valor2
            print('Entre {} e {} o maior valor é: {}.'.format(valor1, valor2, maior))
            print('')
        elif valor1 == valor2:
            print('Entre {} e {} não há valor maior. Ambos são iguais em grandeza.'.format(valor1, valor2, maior))
            print('')
        print('Pressione 9 para rever as opções.')
        opção = int(input('Qual opção você escolhe? '))
    elif opção == 9:
        print('''
        [1] Somar;
        [2] Multiplicar;
        [3] Novos Números;
        [4] Dividir;
        [5] Elevar nº1 ao n2º;
        [6] Elevar nº2 ao nº1;
        [7] Maior Número;
        [8] Sair do Programa.''')
        print('')
        opção = int(input('Qual opção você escolhe? '))
    else:
        print('\033[31mOpção Inválida\033[m. Por favor, selcione uma opção entre 1 e 8.')
        print('')
        print('Pressione 9 para rever as opções.')
        opção = int(input('Qual opção você escolhe? '))
print('')
print('\033[35;46mChegamos ao fim!\033[m')

#A seguir vemos a maneira como o Guanabara resolveu o exercício:
#P. S.: Precisei copiar o código para definir o maior. O meu código não consegue definir o primeiro número como o maior.

n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opção = 0
while opção != 5:
    print('''
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos Números
    [5] Sair do Programa''')
    opção = int(input('Qual é a sua opção? '))
    if opção == 1:
        soma = n1 + n2
        print('A soma entre {} + {} é igual a: {}.'.format(n1, n2, soma))
    elif opção == 2:
        produto = n1 * n2
        print('O resultado de {} x {} é igual a: {}.'.format(n1, n2, produto))
    elif opção == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Entre {} e {} o maior número é: {}.'.format(n1, n2, maior))
    elif opção == 4:
        print('Informe os números novamente: ')
        n1 = int(input('Primeiro número: '))
        n2 = int(input('Segundo valor: '))
    elif opção == 5:
        print('Finalizando...')
    else:
        print('Opção Inválida. Tente novamente.')
    print('=-=' * 10)
print('Fim do programa! Volte sempre!')
