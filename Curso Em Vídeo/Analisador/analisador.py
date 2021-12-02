print('Analisador (Versão Com Dicas e Correções)')
print()
mcontador = 0
fcontador = 0
maioridadeg = 0
maioridade = 0
médiaidade = 0
somamédiaidade = 0
nomemaisvelho = ''
for c in range(1, 4):
    print('-' * 5, '{}ª Pessoas'.format(c), '-' * 5)
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ')
    if sexo in 'Ff':
        fcontador += 1
    elif sexo in 'Mm':
        mcontador += 1
    if idade > 21:
        maioridadeg += 1
    if sexo == 'Mm' or 'Ff':
        médiaidade +=1
        somamédiaidade = idade / médiaidade
    '''if c == 1 and sexo in 'Ff Mm': #Repita exatamente assim para não se ter mais erros.
        maioridade = idade
        nomemaisvelho = nome''' #Essa linha de código é dispensável.
    if sexo in 'Ff Mm' and idade > maioridade: #Também posso usar aquela velha combinação: sexo == 'F M' | [com .upper()]
        maioridade = idade
        nomemaisvelho = nome
print('')
print('O número de pessoas acima da maior idade é de: {}.'.format(maioridadeg))
print('O número de mulheres é de: {} e o número de homens é de: {}.'.format(fcontador, mcontador))
print('A média de idade das pessoas nesse grupo é de: {}.'.format(somamédiaidade))
print('A pessoa mais velha do grupo é: {}.'.format(nomemaisvelho))
