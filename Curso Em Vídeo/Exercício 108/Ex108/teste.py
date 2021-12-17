#Resolução do Guanabara:

print('Formatando Moedas Em Python')
print()

import moeda

p = float(input('Digite um preço: R$'))
print(f'A metade de {p} é igual a: {moeda.metade(p)}.')
print(f'O dobro de {p} é igual a: {moeda.dobro(p)}.')
print(f'Aumentando o valor {p} em 10%, temos: {moeda.aumentar(p, 10):.2f}.')
print(f'Diminuindo o preço {p} em 10%, temos: {moeda.diminuir(p, 10):.2f}.')
