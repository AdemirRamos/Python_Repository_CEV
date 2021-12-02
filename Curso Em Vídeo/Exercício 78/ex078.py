print('Maior e Menor Valores Em Uma Lista')
print('')
valores = [int(input(f'Digite o 1ª valor: ')), int(input(f'Digite o 2ª valor: ')), int(input(f'Digite o 3ª valor: ')),
           int(input(f'Digite o 4ª valor: '))]
print('')
print(f'Os valores digitados foram: {valores}.')
print('')
print(f'O maior valor, dentre os valores digitados, foi "{max(valores)}". Posição: {valores.index(max(valores)) + 1}ª posição.')
print(f'O menor valor, dentre os valores digitados, foi "{min(valores)}". Posição: {valores.index(min(valores)) + 1}ª posição.')

# Resolução do Guanabara:

lista_números = list()
maior = menor = 0
for c in range(0, 5):
    lista_números.append(int(input('Digite um valor para a posição {c}: ')))
    if c == 0:
        maior = menor = lista_números[c]
    else:
        if lista_números[c] > maior:
            maior = lista_números[c]
    if lista_números[c] < menor:
        menor = lista_números[c]

    print(f'Você digitou os valores: {lista_números}.')
    print(f'O maior valor digitado foi "{maior}". Posição: {c}ª posição (ões).', end='')
    for i, v in enumerate(lista_números):
        if v == maior:
            print(f'{i}... ', end='')
            print()
    print(f'O menor valor digitado foi "{menor}". Posição: {c}ª posição (ões).', end='')
    for i, v in enumerate(lista_números):
        if v == menor:
            print(f'{i}... ', end='')
            print()
