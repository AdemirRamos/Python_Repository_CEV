print('Gerenciador de Pagamentos')
print('')
print ('{:=^48}'.format(' Lojas Ademir '))
print('')
valor = float(input('Informe o valor das compras: R$'))
print('''Formas de Pagamento:

[1] À vista dinheiro / Cheque;
[2] À vista no cartão;
[3] Parcelado no Cartão.''')
print('')
pagamento = int(input('Qual é a forma de pagamento? '))
if pagamento == 1:
    desconto = valor - (valor * 10 / 100)
    print('O valor total das compras será de: R${:.2f}.'.format(valor))
    print('Com um desconto de 10%, o valor total passa a ser de: {}.'.format(desconto))
elif pagamento == 2:
    desconto = valor - (valor * 5 / 100)
    print('O valor total das suas compras será de: R${:.2f}'.format(valor))
    print('Com um desconto de 5%, o valor total passa a ser de: {}.'.format(desconto))
elif pagamento == 3:
    parcelas = int(input('Em quantas parcelas será feita a compra? '))
    if parcelas == 2:
        valorpar = valor / 2
        print('O valor da sua compra será de: {:.2f}.'.format(valor))
        print('A sua compra terá 2 parcelas e cada uma custará R${}.'.format(valorpar))
    elif parcelas > 2:
        juros = valor + (valor * 20 / 100)
        valorpar = juros / parcelas
        print('O valor total da sua compra será de: {:.2f} (acréscimo de 20% de juros).'.format(juros))
        print('A sua compra terá um total de {} parcelas e cada parcela vai custar R${:.2f}.'.format(parcelas, valorpar))
else:
    print('\033[031mOpção Inválida. Por favor, tente novamente.\033[m')
