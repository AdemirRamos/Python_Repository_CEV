print('Extraindo Dados De Uma Lista')
print('')
valores = []
valores.append(int(input('Digite um valor: ')))
continuação = input('Você deseja continuar adicionando números? [S/N]: ').strip().upper()
while True:
    valor = int(input('Digite um valor: '))
    valores.insert(0, valor)
    continuação = ' '
    while continuação not in 'SN':
        continuação = input('Você deseja continuar adicionando números? [S/N]: ').strip().upper()
    if continuação in 'N':
        break
print('')
print(f'O valores digitados, na ordem decrescente, ficam assim: {valores}.')
print(f'O total de elementos na lista é de: {len(valores)}.')
print(f'O valor cinco está na {valores.index(5) + 1}ª posição.')

#Resolução do Guanabara
#Eu esqueci que eu deveria colocar os números em ordem decrescente.
#Também esqueci de colocar uma opção para o caso do cindo não estar na lista:

valores = []
while True:
    valores.append(int(input('Digite um valor: ')))
    resposta = str(input('Quer continuar? [S/N]: '))
    if resposta in 'Nn':
        break
print('')
print(f'Você digitou {len(valores)} elementos.')
valores.sort(reverse = True)
print(f'Os valores em ordem decrescente são: {valores}.')
if 5 in valores:
    print('O valor "5" faz parte da lista.')
else:
    print('O valor "5" não foi encontrado na lista.')
