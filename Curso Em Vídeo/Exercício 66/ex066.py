print('Vários Números Com "Flag"')
print('')
cont = soma = 0
while True:
    n = int(input('Digite um número [digite 999 para parar]: '))
    if n == 999:
        break
    soma += n
    cont += 1
print('')
print('A soma entre os números que você digitou (menos 999) é igual a: {}.'.format(soma))
print(f'Ao todo, você digitou {cont} números (menos o número 999).')

#A seguir, temos a maneira como o Guanabara resolveu o exercício:

soma = cont = 0
#Se while True: pode-se remover a variável "n = 0" - Eu a removi da primeira linha do código.
while n != 999:
    num = int(input('Digite um valor (999 para parar): '))
    if num == 999:
        break
    cont += 1
    soma += 1
#soma -= 999 -> Essa é a "maneira gambiarra" de se resolver esse problema (da contagem do 999).
print(f'A soma dos {cont}valores foi de {soma}.')
