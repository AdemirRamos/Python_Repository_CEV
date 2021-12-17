#Resolução do Guanabara:

print('Formatando Moedas Em Python (Parte 2)')
print()

import moeda

p = float(input('Digite um preço: R$'))
print(f'A metade de {moeda.moeda(p)} é igual a: {moeda.metade(p, True)}.')
print(f'O dobro de {moeda.moeda(p)} é igual a: {moeda.dobro(p, True)}.')
print(f'Aumentando o valor {moeda.moeda(p)} em 10%, temos: {moeda.aumentar(p, 10, True)}.')
print(f'Diminuindo o preço {moeda.moeda(p)} em 13%, temos: {moeda.diminuir(p, 13, True)}.')
