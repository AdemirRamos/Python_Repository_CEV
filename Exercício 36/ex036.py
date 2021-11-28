print('Aprovando Empréstimo')
print()
casa = float(input('Digite o quanto vale a casa: R$'))
salário = float(input('Digite o salário do comprador: R$'))
anos = int(input('Digite quantos anos o comprador vai levar para pagar (financiamento): '))
prestação = casa / (anos * 12)
mínimo = salário * 30 / 100
print('Para pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f}.'.format(casa, anos, prestação))
if prestação <= mínimo:
    print('O seu empréstimo foi aprovado/concedido.')
else:
    print('O seu empréstimo foi recusado/negado.')
