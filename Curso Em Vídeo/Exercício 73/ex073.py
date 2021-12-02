print('Tuplas Com Times De Futebol')
print('')
print('Esta é a tabela do Brasileirão 2021:')
tabela = 'Atlético-MG', 'Flamengo', 'Fortaleza', 'Palmeiras', 'Red Bull Bragantino', 'Corinthians', \
        'Internacional', 'Fluminense,', 'Cuiabá', 'Athletico-PR', 'Atlético-GO', 'São Paulo', 'América-MG',\
        'Ceará', 'Santos', 'Bahia', 'Juventude', 'Sport', 'Grêmio', 'Chapecoense'
print('')
print('Os cinco primeiros classificados são: ')
print('')
for c in range(0, 4):
    print(f'{c + 1}ª', tabela[c])
print('')
print('Os cinco útimos colocados são: ')
print('')
for c in range(19, 14, -1):
    print(f'{c + 1}ª', tabela[c])
print('')
#print(f"A posição da Chapecoense é: {tabela.index('Chapecoense') + 1}ª.")
print(f"Na {tabela.index('Chapecoense') + 1}ª posição temos a Chapecoense.")

#Resolução do Guanabara:

print('Tuplas Com Times De Futebol')
print('')
times = 'Atlético-MG', 'Flamengo', 'Fortaleza', 'Palmeiras', 'Red Bull Bragantino', 'Corinthians', \
        'Internacional', 'Fluminense,', 'Cuiabá', 'Athletico-PR', 'Atlético-GO', 'São Paulo', 'América-MG',\
        'Ceará', 'Santos', 'Bahia', 'Juventude', 'Sport', 'Grêmio', 'Chapecoense'
print('-=' * 15)
print(f'Lista de times: {times}.')
print('-=' * 15)
print(f'Os cinco primeiros são: {times[0:5]}.')
print('-=' * 15)
print(f'Os quatro últimos são: {-4:}.')
print('-=' * 15)
print(f'Times em ordem alfabética: {sorted(times)}.')
print('-=' * 15)
print(f'A Chapecoense está na {times.index("Chapecoense") + 1}ª posição.')
print('-=' * 15)
#Outra opção aqui, seria usar o ".format()" ao invés de "f strings".
