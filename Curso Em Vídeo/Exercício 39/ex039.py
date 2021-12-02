print('Alistamento Militar')
print('')
print('Informe o seu sexo.')
print('')
print('[1] para "masculino";\n[2] para "feminino".')
print('')
sexo = int(input('Digite aqui: '))
print('')
#sexo = input('Digite o seu sexo: ').strip().upper()
#if sexo == 'MASCULINO':
if sexo == 1:
    print('Você é do sexo "masculino". O alistamento é obrigatório somente para homens.', end='')
    print(' Agora, vamos continuar.')
    print('')
    birth = int(input('Digite o seu ano de nascimento: '))
    ano = 2017
    idade = ano - birth
    print('Quem nasceu em {} tem {} anos de idade em {}.'.format(birth, idade, ano))
    if idade == 18:
        print('Você tem 18 anos de idade portanto deve se apresentar ao Alistamento Militar.')
    elif idade < 18:
        print('Você ainda não completou 18 anos.', end="")
        faltam = 18 - idade
        print(' Ainda falta (m) {} ano (s) para você se apresentar ao Alistamento Militar.'.format(faltam))
        data = ano + faltam
        print('O seu ano de alistamento será em {}.'.format(data))
    elif idade > 18:
        print('\033[31mJá passou da sua hora de se alistar! Procure o posto de alistamento\033[m', end="")
        print(' \033[31mmais próximo o quanto antes.\033[m')
        atraso = idade - 18
        print('\033[31mVocê está com {} ano (s) de atraso.\033[m'.format(atraso))
        data = ano - atraso
        print('\033[34mO seu ano de alistamento foi em {}.\033[m'.format(data))
elif sexo == 2:
    #elif sexo == 'FEMININO':
    print('O alistamento é obrigatório somente para homens.')
    print('Tenha um bom dia.')
else:
    print('Por favor, tente outra vez.')

'''idade = int(input('Digite a sua idade: '))
resto = 18 - idade
print(resto)'''

#A seguir, vai a maneira como o Guanabara resolveu o exercício:

print('')
from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}.'.format(nasc, idade, atual))
if idade == 18:
    print('Você tem que se alistar imediatamente!')
elif idade < 18:
    saldo = 18 - idade
    print('Você ainda não tem 18 anos. Ainda faltam {} anos para o alistamento.'.format(saldo))
    ano = atual + saldo
    print('O seu alistamto será em {}.'.format(ano))
elif idade > 18:
    saldo = idade - 18
    print('Você já deveria ter se alistado há {} anos.'.format(saldo))
    ano = atual - saldo
    print('O seu ano de alistamento foi em {}.'.format(ano))
