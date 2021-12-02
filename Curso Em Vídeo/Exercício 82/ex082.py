print('Dividindo Valores Em Várias Listas')
print('')
valores = list()
valores_par = list()
valores_impar = list()
valores.sort(reverse=True)
while True:
    valor = int(input('Digite algum valor: '))
    valores.append(valor)
    continuação = input('Você deseja continuar adicionando números à lista? [S/N]: ').strip().lower()
    if valor % 2 == 0:
        valores_par.append(valor)
    else:
        valores_impar.append(valor)
    if continuação in 'n':
        break
    elif continuação not in 'ns':
        print('Erro.')
        break
print('')
print(f'Os valores digitados foram: {valores}')
print(f'Os valores pares digitados foram: {valores_par}.')
print(f'Os valores ímpares digitados foram: {valores_impar}.')

# Resolução do Guanabara:

números = list()
pares = list()
ímpares = list()
while True:
    números.append(int(input('Digite um número: ')))
    resposta = str(input('Quer continuar? [S/N]'))
    if resposta in 'Nn':
        break
for i, v in enumerate(números):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        ímpares.append(v)
    # Essa linha, acima, também poderia ser escrita assim: else: ímpares.append(v) - P.S.: Essa não é uma linha simplificada.

print('')
print(f'A lista completa é {números}.')
print(f'A lista de pares é: {pares}.')
print(f'A lista de ímpares é: {ímpares}.')
