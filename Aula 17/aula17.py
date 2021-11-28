print('Listas (Parte 1)')
print('')

números = (2, 5, 9, 1)
#Essa é uma Tupla.
print(números)

números_lista = [2, 5, 9, 1]
números_lista[2] = 3
#Listas, diferente de Tuplas, são mutáveis.

#números_lista[4] = 7. Esse comando não irá funcionar pois não se pode adicionar um novo elemento a uma lista em uma posição não existente previamente.
números_lista.append(7)
#Para se adicionar um novo elemento (ainda não existente) à lista, se usa esse comando acima ['append()].

números_lista.sort()
#Organiza os elementos da lista - números em ordem crescente; letras em ordem alfabética.

números_lista.sort(reverse = True)
#Organiza os elementos da lista com a mesma lógica do método anterior, porém de trás para frente (em order reversa).

números_lista.insert(2, 0)
#Também adiciona novos elementos à lista. Nesse caso, na segunda posição da lista, será adicionado o valor 0 (zero).

números_lista.pop()
#Remove o último elemento da lista.

números_lista.pop(2)
#Remove o segundo elemento da lista.

números_lista.insert(2, 2)
números_lista.remove(2)
#Nesse caso, o "remove" removerá somente a primeira ocorrência encontrada do elemento buscado.
#Caso se tente remover um elemento que não está na lista, ocorrerá um erro.
#Uma solução para esse problema seria:

if 4 in números_lista:
    números_lista.remove(4)
else:
    print('Valor não encontrado')

print(f'Esta lista tem {len(números_lista)} elementos.')
#Esse método mostra o tamanho da lista.

print(números_lista)

valores = list()
#Uma lista vazia pode ser iniciada de uma destas duas maneiras: valores = [] / valores = list().

valores.append(5)
valores.append(9)
valores.append(4)

print(valores)

for v in valores:
    print(f'{v}...', end='')

for c, v in enumerate(valores):
    print(f'Na posição {c} foi encontrado o valor {v}...')
#Enúmera e mostra os índices dos elementos da lista.
print('Fim da lista.')

for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))

for c, v in enumerate(valores):
    print()
    print(f'Na posição {c} foi encontrado o valor {v}...')
#Enúmera e mostra os índices dos elementos da lista.
print('')
print('Fim da lista.')
#É requisitada a digitação de valores e, após isso, são apresentados os valores na tela.

a = [2, 3, 4, 7]
b = a
print(f'Lista A: {a}.')
print(f'Lista B: {b}.')
#A mesma lista será "printada" duas vezes pois não há diferença entre "a" e "b".

a = [2, 3, 4, 7]
b = a
b[2] = 8
print(f'Lista A: {a}.')
print(f'Lista B: {b}.')
#A alteração ("b" recebendo 8), será feita em ambas as listas. Em Python, uma vez que se iguala duas ou mais listas, o Python cria uma ligação entre as listas.

a = [2, 3, 4, 7]
b = a [:]
#"b" vai receber todos os valores de "a". - Não há marcação de começo nem de fim, por isso "b" recebe todos os valores de "a".
#Assim se cria uma cópia de uma lista.
b[2] = 8
print(f'Lista A: {a}.')
print(f'Lista B: {b}.')
#Agora a alteração "b[2] = 8" será feita somente na lista "b".
