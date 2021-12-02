'''for c in range(6, 0, -1): #O "-1" serve para fazer uma contagem regressiva.
    print(c)
for c in range(0, 6, 2): #O 2 (após o 6) serve para pular de 2 em 2.
    print(c)
for c in range(0, 7): #7 simboliza o fim mas a contagem para no 6.
    print(c)
print('Fim.')
n = int(input('Digite um número: '))
for c in range(0, n+1): #Com "n+1" você faz o Python contar até o número digitado.
    print(c)
print('Fim.')
i = int(input('Digite o ínicio: '))
f = int(input('Digite o fim: '))
p = int(input('Digite o passo: '))
for c in range(i, f+1, p): #Primeiro é indicado o ínicio, depois o fim, e, por último, de quanto em quanto se pulará.
    print(c)
print('Fim.')'''
s = 0
for c in range(0, 3): #Repete o "input" três vezes.
    n = int(input('Digite algum valor: '))
    s += n #s += n == s = s + n.
print('O somatório de todos os valores é: {}.'.format(s))
