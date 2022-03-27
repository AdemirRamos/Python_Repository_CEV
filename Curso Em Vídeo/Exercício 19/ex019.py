print('Sorteando Um Item Na Lista')
print()
import random
n1 = str(input('Digite o nome do (a) primeiro (a) aluno (a): '))
n2 = str(input('Digite o nome do (a) segundo (a) aluno (a): '))
n3 = str(input('Digite o nome do (a) terceiro (a) aluno (a): '))
n4 = str(input('Digite o nome do (a) quarto (a) aluno (a): '))
lista = [n1, n2, n3, n4]
escolhido = random.choice(lista)
print('')
print('O (a) aluno (a) escolhido (a) foi: {}.'.format(escolhido))
print('')
print('Os "str" estão postos OPCIONALMENTE.')
from random import choice
n1 = input('Digite o nome do primeiro aluno: ')
n2 = input('Digite o nome do segundo aluno: ')
n3 = input('Digite o nome do terceiro aluno: ')
n4 = input('Digite o nome do quarto aluno: ')
lista = [n1, n2, n3, n4]
escolhido = choice(lista)
print('')
print('O aluno escolhido foi: {}.'.format(escolhido))
