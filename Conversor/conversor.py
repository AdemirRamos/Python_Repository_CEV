print('Conversão de Valores')
print()
valor = float(input('Digite o valor que você deseja converter: R$'))
cota = float(input('Digite a cotação da moeda: '))
moeda = str(input('Digite a moeda para a qual você quer converter o valor: ').strip().upper())
conver = valor / cota
if moeda == 'DOLAR':
    print('Conversão: US${:.2f}.'.format(conver))
if moeda == 'EURO':
    print('Conversão: {:.2f}€.'.format(conver))
