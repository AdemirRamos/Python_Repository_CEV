import random
print('Exercício 99')
print()
lista = list()
lista_2 = list()

def valores():
    contador = random.randint(0, 10)
    print('Analisando os dados informados...')
    for c in range(0, contador):
        lista.append(contador)
        lista.clear
    print(f'Ao todo, foram informados {len(lista)} valores.')

valores()
print(lista)
print(f'O maior valor, entre os números na lista, foi: {max(lista)}.')
