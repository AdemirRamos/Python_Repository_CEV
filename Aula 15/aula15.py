cont = 1
while cont <= 10:
    print(cont, ' -> ',end='')
    cont += 1
print('Acabou.')

#Se você escrever:
'''while True:
print(cont, ' -> ',end='')
cont += 1
print('Acabou.')'''
#Essa laço se estenderá perpetuamente.

n = cont = 0
while cont < 3:
    n = int(input('Digite um número: '))
    cont += 1

n = s = 0
while n != 999:
    n = int(input('Digite um número: '))
    s += n
s -= 999 #Essa linha de código é uma "gambiarra".
print(f'A soma vale {s}.')

n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break #Esse "break" faz a soma ser mostrada sem somar o 999.
    s += n
print(f'A soma vale {s}.')
print('A soma %s tem %d' % (s, n)) #Forma antiga de usar variáveis em "strings". - Original do Python 2.
salário = 985.35
print(f'O salário é de {salário:.2f}') #Formatação estilo "float".
nome = 'Alguém'
print(f'O nome é {nome:-^20} {nome:->20} {nome:<-20}') #Centralizado, à direita, à esquerda.

n = soma = cont = 0
while True:
    n = int(input('Digite um número [999 irá parar o programa]: '))
    if n == 999:
        break
    soma += n
    cont += 1
print(f'A soma entre os valores digitados (menos 999) é igual a: {soma}.')
print(f'Ao todo, foram digitados {cont} valores.')
