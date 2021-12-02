print('Funções (Parte 1)')
print()

#"def": definição de função. Se usa essa palavra para declarar uma função personalizada.
#"def" == função.
#def mostraLinha(): <- assim se escreve uma função personalizada em Python.
#Em Python, todas as funções (funcionalidades) são identificadas por parênteses no final de seus nomes.
#Primeiro exemplo prático:

def linha():
    print('-=' * 30)

def mensagem(message):
    print('-=' * 30)
    print(message)
    print('-=' * 30)

def título(texto):
    print('-=' * 30)
    print(texto)
    print('-=' * 30)

#As linhas abaixo são chamadas de "programa principal".

print('-=' * 30)
print('Curso Em Vídeo.')
print('-=' * 30)

print('-=' * 30)
print('Aprenda Python.')
print('-=' * 30)

print('-=' * 30)
print('Gustavo Guanabara.')
print('-=' * 30)

linha()
print('Curso de Python.')
linha()

mensagem('Olá, mundo!')
título('Funções Em Python!')

def soma(a, b):
    s = a + b
    print(s)

a = 4
b = 5
s = a + b
print(s)
print()
a = 8
b = 9
s = a + b
print(s)
print()
a = 2
b = 1
s = a + b
print(s)
print()

#Programa principal:

soma(4, 5)
soma(8, 9)
soma(2, 1)
print()

#A função acima demanda dois parâmetros, caso só exista um, a função não funcionará.

#É possível definir com mais exatidão os parâmetros da função:

def soma_2(c, d):
    s = c + d
    print(s)

soma_2(d = 4, c = 5)
print()

def soma_3(e, f):
    print(f'E = {e} e F = {f}.')
    s = e + f
    print(f'A soma entre E + F é igual a: {s}.')

soma_3(5, 7)
soma_3(e = 7, f = 9)
print()
#Não é possível explicitar somente um dos parâmetros. Ou isso é feito com ambos ou com nenhum.
#Exemplo: "soma_3(e = 7, 5)".
#Mais uma ressalva: se a sua função tem dois parâmetros e a sua chamada três, ocorrerá um erro.
#O número de parâmetros da chamada e da função deve ser iguais.

#Empacotar Parâmetros:

def contador(* núm):
#O asterisco indica que parâmetros serão definidos na chamada da função e, todos esses parêmtros, irão para o parâmetro formal "núm".
#Dessa maneira, se pode adicionar quantos parâmetros formais se desejar.
    print(f'Os números digitados foram: {núm}.')
    for valor in núm:
        print(valor, end=' ')
    print('Fim!')
    tamanho = len(núm)
    print(f'Os valores digitados foram: {núm}. Ao todo, os números digitados nesta chamada foram: {tamanho}.')

contador(5, 7, 3, 1, 4)
print()
contador(8, 4, 7)
print()

def dobrar(lista):
    posição = 0
    while posição < len(lista):
        lista[posição] *= 2
        posição += 1

valores = [7, 2, 5, 0, 4]
dobrar(valores)
print(valores)
print()

def soma(* valores):
    soma = 0
    for num in valores:
        soma += num
    print(f'Somando os valores {valores}, temos a seguinte soma: {soma}.')

soma(5, 2)
soma(2, 9, 4)
print()
