print('Números Por Extenso')
print('')
while True:
    números = int(input('Digite um número entre 0 e 20: '))
    números_por_extenso ='Zero.', 'Um.', 'Dois.', 'Três.', 'Quatro.', 'Cinco.',\
                         'Seis.', 'Sete.', 'Oito.', 'Nove.', 'Dez.',\
                         'Onze.', 'Doze.', 'Treze.', 'Quatorze ou Catorze.', 'Quinze.',\
                         'Dezesseis.', 'Dezessete.', 'Dezoito.', 'Dezenove.', 'Vinte.'
    print('Você digitou o número', números_por_extenso[números])
    print('')

#Resolução do Guanabara:

cont = 'Zero.', 'Um.', 'Dois.', 'Três.', 'Quatro.', 'Cinco.',\
       'Seis.', 'Sete.', 'Oito.', 'Nove.', 'Dez.',\
       'Onze.', 'Doze.', 'Treze.', 'Quatorze ou Catorze.', 'Quinze.',\
       'Dezesseis.', 'Dezessete.', 'Dezoito.', 'Dezenove.', 'Vinte.'
while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if 0 <= num <= 20: #se o número estiver entre 0 e 20, interrompa (o laço).
        break
    print('Tente novamente. ', end='')
print(f'Você digitou o número {cont[num]}')
