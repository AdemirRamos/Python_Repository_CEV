print('Estatísticas Em Produtos')
print('')
print('=-' * 10)
print('Lojas Super Baratão')
print('=-' * 10)
contador_total = quantidade = menor_preço = maior_preço = 0
while True:
    print('')
    produto = input('Nome do produto: ')
    preço = int(input('Preço do produto: R$'))
    continuação = ' '
    while continuação not in 'sn':
        print('')
        continuação = input('Você quer continuar? [S/N]: ').strip().lower()[0]
    contador_total += preço
    quantidade += 1

    if quantidade == 1:
        menor_preço = preço
        cheapest_name = produto
    else:
        if preço < menor_preço:
            menor_preço = preço
            cheapest_name = produto
    if preço > 1000:
        maior_preço += 1
    if continuação in 'n':
        break


print('')
print('Fim do Programa.')
print('')
print('O total da compra foi de: \033[031mR${:.2f}\033[m.'.format(contador_total))
print('Produto (s) acima de R$1,000,00: \033[031m{}.\033[m'.format(maior_preço))
print('O produto mais barato (\033[031m{}\033[m) custou \033[031mR${:.2f}\033[m.'.format(cheapest_name, menor_preço))

#Para fazer "maior" e "menor", eu precisei recorrer a ajuda externa; idem para o nome do produto mais barato.
#Resolução do Guanabara:

total = totmil = menor = cont = 0
barato = ' '
while True:
    produto = str(input('Nomde do produto: '))
    preço = float(input('Preço: R$'))
    cont += 1
    total += preço
    if preço > 1000:
        totmil += 1
    if cont == 1: #or if preço < menor: -> essa linha de código simplifica o programa e dispensa o intervalo entre 53 e 56.
        menor = preço
        barato = produto
    else:
        if preço < menor:
            menor = preço
            barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break
print('{:-^40}'.format(' Fim do programa. '))
print(f'O total da compra foi R${total:.2f}.') #-> total:10.2f: dez casas (ao t0do) e duas decimais em ponto flutuante.
print(f'Temos {totmil} produtos custando mais de R$1,000,00.')
print(f'O produto mais barato (a) ({barato}) custa R${menor:.2f}.')
