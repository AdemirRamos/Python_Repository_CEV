print('Exercício 101')
print()
def voto():
    nascimento = int(input('Digite o seu ano de nascimento: '))
    idade = 2021 - nascimento
    if idade < 16:
        print(f'Você tem {idade} anos de idade. Você tem menos de 16 anos. Para você, o voto não é obrigatório nem facultativo.')
    elif idade <= 17:
        print(f'Você tem {idade} anos de idade. A sua idade está entre 16 e 18 anos. Para você, o voto é facultativo.')
    elif idade < 65:
        print(f'Você tem {idade} anos de idade. A sua idade está entre 18 e 65 anos. Para você, o voto é obrigatório.')
    else:
        print(f'Você tem {idade} anos de idade. A sua idade é maior do que 65 anos. Para você, o voto é facultativo.')
voto()