preço = float(input('Digite o valor do produto: R$'))
desconto = float(input('Digite o valor do desconto: %'))
off = preço - (preço * desconto / 100)
print('O preço total, após o desconto, é de: R${:.2f}.'.format(off))
print('')
tef = float(input('Digite a temperatura em ºF: '))
conversão = (tef - 32) * 5 / 9
print('Temperatura: {:.2f}ºF.'.format(conversão))
print('')
tec = float(input('Digite a temperatura em ºC: '))
conver = (tec * 9 / 5) + 32
print('Conversão: {:.2f}ºC'.format(conver))
print('')
valor = float(input('Digite o valor do produto: R$'))
desconto = float(input('Digite o valor do desconto: %'))
off = valor - (valor * desconto / 100)
print('O produto, após os descontos, fica no valor de: R${:.2f}.'.format(off))
