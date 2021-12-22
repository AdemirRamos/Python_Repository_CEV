print('Conversor de Moedas')
print()

valor = float(input('Digite um valor (em reais) para convertê-lo em dólares: R$'))
conversão = valor / 5.75 #Valor do dólar em 21/12/2021.
print(f'\nA conversão do valor digitado fica igual a: US${conversão:.2f}.')
