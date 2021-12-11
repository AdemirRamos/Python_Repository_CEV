print('Função Que Descobre o Maior Número')
print()
import random
lista = list()
lista_2 = list()

def valores():
    contador = random.randint(1, 10)
    print('Analisando os dados informados...')
    for c in range(1, contador):
        contador = random.randint(1, 10)
        lista.append(contador)
        lista.clear
    print(f'Ao todo, foram informados {len(lista)} valores.')

valores()
print(lista)
print(f'O maior valor, entre os números na lista, foi: {max(lista)}.')

#Resolução do Guanabara:

print('Função Que Descobre o Maior Número')
print()

from time import sleep

def maior(* valores):
    cont = maior = 0
    print('-=' * 30)
    print('Analisando os valores passados...')
    for valor in valores:
        print(f'{valor}', end=' ')
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram informados {valores} e o maior valor foi: {maior}.')

maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior(0)
