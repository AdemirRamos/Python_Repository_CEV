print ('{:=^48}'.format(' Lojas Guanabara '))
print('')
preço = float(input('Informe o valor das compras: R$'))
print('''Formas de Pagamento:

[1] À vista dinheiro / Cheque;
[2] À vista no cartão;
[3] 2x cartão;
[4] 3x ou mais no catão.''')
print('')
pagamento = int(input('Qual é a forma de pagamento? '))
if pagamento == 1:
    total = preço - (preço * 10 / 100)
elif pagamento == 2:
    total = preço - (preço * 5 / 100)
elif pagamento == 3:
    total = preço
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R${:.2f} (sem juros).'.format(parcela))
elif pagamento == 4:
    total = preço + (preço * 20 / 100)
    totparc = int(input('Em quantas parcelas será feita a compra? '))
    parcela = total / totparc
    print('Sua compra será parcelada em {}x R${:.2f} (com juros de 20%).'.format(totparc, parcela))
else:
    total = preço
    print('\033[31mOpção Inválida. Tente novamente.\033[m')
print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preço, total))
