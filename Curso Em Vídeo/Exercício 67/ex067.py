print('Taboada (Versão 3.0)')
print('')
cont = 0
print('Antes de começarmos, lembre-se: para parar, basta digitar um número negativo.')
print('')
n = int(input('Digite um número para ver a sua taboada: '))
while cont < 10:
    cont += 1
    multi = n * cont
    if n < 0:
        break
    print(f'A taboada do {n} fica assim: {n} x {cont} = {multi}')
print('Chegamos ao fim da taboada!')

#Minha resolução ficou incompleta. Vou precisar recorrer ao Guanabara.

while True:
    n = int(input('Quer ver a taboada de qual valor? Digite aqui: '))
    print('-' * 30)
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{n} x {c} = {n*c}.')
    print('-' * 30)
print('Fim.')
