print('Valores Únicos Em Uma Lista')
print()
valor = int(input('Digite algum valor: '))
continuação = input('Você deseja continuar adicionando valores? [S/N]: ').strip().upper()
valores_lista = []
valores_lista.insert(0, valor)
while True:
    valor = int(input('Digite algum valor: '))
    valores_lista.append(valor)
    if valor == valores_lista[0]:
        print('Valor repetido! Por favor, digite outro valor.')
        print('')
        valores_lista.remove(valor)
    continuação = input('Você deseja continuar adicionando valores? [S/N]: ').strip().upper()
    if continuação in 'N':
        break
    elif continuação not in 'SN':
        print('Erro! Opção digitada inválida.')
        break
valores_lista.sort()
print(f'Os valores digitados foram: {valores_lista}.')

#Resolução do Guanabara:

números = list()
while True:
    número = int(input('Digite algum valor: '))
    if número not in números:
        números.append(número)
        print('Valor adicionado.')
    else:
        print('Valor duplicados não serão adicionados.')
    resposta = str(input('Deseja adicionar mais valores? [S/N].strip().lower()'))
    if resposta in 'n':
        break
números.sort()
print('Você digitou os seguintes valores: {números}.')
