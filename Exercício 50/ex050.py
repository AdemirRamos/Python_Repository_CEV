print('Soma Dos Pares')
print()
soma = 0
count = 0
for pares in range(2, 7, 2):
    print(pares)
if pares % 2 == 0:
    soma += pares
    count = pares - 3
    print('A soma entre esses {} números pares é igual a: {}.'.format(count, soma))
print('Esses são os pares de 1 a 6 junto de sua soma.')

#Eu não entendi bem o exercício. - O exercício acima, pórém, não está errado. (...) A seguir vai o que foi pedido:

print()
soma = 0
count = 0
for c in range(1, 7):
    num = int(input('Digite um valor: '))
    if num % 2 == 0:
        soma += num
        count += 1
print('Você informou {} números pares e a soma entre eles foi de {}.'.format(count, soma))
