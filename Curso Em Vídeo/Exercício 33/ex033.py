print('Maior e Menor Valores')
print()
a = int(input('Digite o primiero valor: '))
b = int(input('Digite o segundo valor: '))
c = int(input('Digite o terceiro valor: '))
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
print('Dentre os valores digitados, o menor foi: {}.'.format(menor))
print()
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('Dentre os valores digitados, o maior foi: {}.'.format(maior))
