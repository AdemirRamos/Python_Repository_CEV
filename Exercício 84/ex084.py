print('Lista Composta e Análise De Dados')
print()
lista_temporária = []
lista_principal = []
maior = menor = 0
#Se você fizer "lista_temporária = lista_principal = []" será gerada uma conexão entre as listas.
while True:
    lista_temporária.append(str(input('Nome: ')))
    lista_temporária.append(float(input('Peso: ')))
    if len(lista_principal) == 0:
        maior = menor = lista_temporária[1]
    else:
        if lista_temporária[1] > maior:
            maior = lista_temporária[1]
        if lista_temporária[1] < menor:
            menor = lista_temporária[1]
    lista_principal.append(lista_temporária[:])
    lista_principal.clear()
    resposta = str(input('Você deseja continuar? [S/N]: ')).strip().upper()
    if resposta in 'N':
        break
#print(f'Os dados foram: {lista_principal}.')
print(f'Ao todo, você cadastrou {len(lista_principal)} pessoas.')
print(f'O maior peso encontrado foi: {maior}. Pessoas que apresentaram esse peso: ', end='')
for p in lista_principal:
    if p[1] == maior:
        print(f'{p[0]}.', end='')
print(f'O menor peso encontrado foi: {menor}. Pesoas que apresentarem esse peso: ', end='')
for p in lista_principal:
    if p[1] < menor:
        print(f'{p[0]}.', end='')
