#Resolução do Guanabara:

print('Exercitanto Módulos Em Python')
print()

import moeda

p = float(input('Digite um preço: R$'))
print(f'A metade de R${p} é igual a: R${moeda.metade(p)}.')
print(f'O dobro de R${p} é igual a: R${moeda.dobro(p)}.')
print(f'Aumentando o valor R${p} em 10%, temos: R${moeda.aumentar(p, 10):.2f}.')
print(f'Diminuindo o preço R${p} em 10%, temos: R${moeda.diminuir(p, 10):.2f}.')
