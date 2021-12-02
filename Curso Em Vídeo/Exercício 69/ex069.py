print('Análise De Dados Do Grupo')
print('')
print('Cadastre uma pessoa: ')
print('')
contador_idade = 0
homem_total = 0
mulher_menos_de_vinte = 0

while True:
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ').strip().lower()[0]
    print('')
    continuação = input('Quer continuar? [Sim/Não]: ').strip().lower()[0]
    print('')

    if idade > 18:
        contador_idade += 1
    if sexo in 'm':
        homem_total += 1
    elif idade < 20:
        if sexo in 'f':
            mulher_menos_de_vinte += 1
    if continuação in 'n':
        break
    elif continuação not in 'sn':
        print('\033[031mErro!\033[m')
        break

print('')
print(f'O total de pessoas cadastradas com mais de 18 anos é de: {contador_idade}.')
print(f'O total de homens cadastrados foi de: {homem_total}.')
print(f'O total de mulheres com menos de vinte (20) anos foi de: {mulher_menos_de_vinte}.')

#Resolução do Guanabara:

tot18 = totH = totM20 = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]

    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        totH += 1
    if sexo == 'F' and idade < 20:
        totM20 += 1

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {tot18}.')
print(f'Ao todo, temos {totH} homens cadastrados.')
print(f'E temos {totM20} mulheres com menos de 20 anos.')
