print('Tuplas')
print('')
lanche = ('hambúrger', 'suco', 'pizza', 'pudim')
print(lanche)
print(lanche[0])

for comida in lanche:
    print(f'Eu vou comer {comida}')
print('Comi para caramba!')

print('Total de comidas para o lanche: ', len(lanche))

for c in range(0, len(lanche)):
    print(c)
    print(lanche[c])
    print(f'Eu vou comer {lanche[c]}.')
    print(f'Eu vou comer {lanche[c]} na posição {c}.')

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}.')

#lanche = ('hambúrger', 'suco', 'pizza', 'pudim'). Fiz esse comentário só para ter a referência de tupla.

print(sorted(lanche))
#sorted: organiza os elementos da tupla (em ordem alfabética).
#Porém, para fazer essa alteração, a variável vai dexar de ser tupla e vai virar lista.

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c)
#A primeira tupla será escrita na tela; após isso, a segunda tupla também será escrita na tela.

print(len(c))
print(c.count(5))
#Conta o número de repetições do elementos entre parentêses.

print(c.index(8))
#Mostra a posição do elemento entre parentêses.
#Caso um elemento se repita, o "index" caputrará somente a primeira ocorrência do elemento em questão.

print(c.index(2, 4))
#O primeiro elemento (2) indica qual elemento se está buscando;
#O segundo elemento (4) indica a partir de onde será feita a busca pelo elemento procurado.
#O nome desse processo é "deslocamento".

pessoa = ('Gustavo', 39, 'M', 99.88)
#Diferente dos vetores ("arrays") em JS, as tuplas aceitam elementos de diferentes tipos.

print(pessoa)
del(pessoa)
#"del" ("delete") apaga o conteúdo da variável. "del" serve para qualquer outra coisa em Python.
