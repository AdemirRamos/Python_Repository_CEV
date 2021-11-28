print('Simulador de Dados')
print('')
import random
soma_dados = valor_total = 0
while True:
    quantos_dados = int(input('Quantos dados você quer jogar? 1 ou 2? '))
    print('')
    if quantos_dados == 1:
        dado_1 = random.randint(1, 6)
        print(f'O resultado do primeiro dado foi: {dado_1}.')
        valor_total_1 = dado_1
        print('')
        continuação = input('Quer continuar? (Digite "não" para parar o programa / "sim" para continuar): ').strip().lower()[0]
        print('')
        while continuação not in 'ns':
            print('Erro.')
            print('')
            continuação = input('Quer continuar? (Digite "não" para parar o programa / "sim" para continuar): ').strip().lower()[0]
            print('')
        if continuação in 'n':
            break
    elif quantos_dados == 2:
        dado_1 = random.randint(1, 6)
        dado_2 = random.randint(1,6)
        soma_dados = dado_1 + dado_2
        print(f'O resultado do primeiro dado foi: {dado_1}.')
        print(f'O resultado do segundo dado foi: {dado_2}.')
        print(f'A soma do valor do primeiro dado mais o valor do segundo dado é: {soma_dados}.')
        print('')
        continuação = input('Quer continuar? (Digite "não" para parar o programa / "sim" para continuar): ').strip().lower()[0]
        print('')
        while continuação not in 'ns':
            print('Erro.')
            print('')
            continuação = input('Quer continuar? (Digite "não" para parar o programa / "sim" para continuar): ').strip().lower()[0]
            print('')
        if continuação in 'n':
            break
print('Fim do programa. Obrigado por jogar.')
