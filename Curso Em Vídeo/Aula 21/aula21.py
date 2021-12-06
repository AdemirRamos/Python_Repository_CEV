print('Funções (Parte 2)')
print()

print('Interactive Help:')
#Para conseguir ajuda interativa, basta usar o comando/funcionalidade interna [do Python] "help()".
#Toda vez que abrimos e fechamos parênteses após alguma palavra, isso quer dizer que a palavra em questão é uma função.
#P. S.: Os comando "help" foram definidos como comentários apenas para não "atrapalhar" a execução do programa. 

#help()

#P. S.: "help()" só funciona no terminal / console.
#Digite "quit" na "interactive help" para voltar ao "Python interpreter".
#Outra maneira de se conseguir ajuda para saber o que algum comando faz:

#help(print)

#Outra maneira de se conseguir ajuda é através do "doc":

#print(input.__doc___)
#help(input)

#As informações de ambos comando acima podem variar.

print('Docstrings:')

#Uma "docstring" é, basicamente, uma "string" de documentação.
#Exemplo:

def contador(i, f, p):
    """
    
    -> A função contador faz com que o programa realize uma contagem, com base nos valores digitados pelo usuário, e a exiba na tela. 

    :param i: início da contagem;
    :param f: fim da contagem;
    :param p: passo da contagem;
    :return: sem retorno. 

    """
    #Aparentemente, no "Pycharm", as "docstrings" vão seguir, mais ou menos, o modelo acima.

    c = i
    while c <= f:
        print(f'{c}', end='... ')
        c += p
    print('Fim!')

contador(2, 10, 2)
#help(contador)

#Através das "docstrings", você pode gerar uma ajuda interativa com explicações sobre a sua função.
#A "docstring" sempre começa após o comando "def".
#Após o comando "def", basta você abrir e fechar aspas duplas 3 vezes e assim você terá a sua "docstring".

print('Parêmetros Opcionais:')

def somar(a = 0, b = 0, c = 0):

    """
    
    A função somar possui três parâmetros opcionais que serão preenchidos caso o usuário digite números para cada parâmetro.
    Após digitados os números, eles serão somados e o resultado será mostrado na tela.
    Caso um ou mais parâmetros não recebam valores, eles, por padrão, manterão o seu valor 0 (zero).

    - Parâmetro "a = 0": é o primeiro parâmetro. Esse parâmetro receberá o primeiro valor digitado pelo usuário;
    - Parâmetro "b = 0": é o segundo parâmetro. Esse parâmetro receberá o segundo valor digitado pelo usuário;
    - Parâmetro "c = 0": é o terceiro parâmetro. Esse parâmetro receberá o terceiro valor digitado pelo usuário;
    - Variável "s": é a responsável por fazer a soma entre os parâmetros;
    - Print: exibe, de maneira formatada, o resultado final da função "contador".

    """

    s = a + b + c
    print(f'A soma é igual a: {s}.')

somar(3, 2, 5)
somar(8, 4)
somar()
somar(b = 4, c = 2) #Podemos definir os parâmetros também aqui.

#Ao se atribuir o valor 0 (zero) a "c", "c" passa a ser um parâmetro opcional.
#Você pode definir todos os seus parâmetros como parâmetros opcionais.

print('Escopo de Variáveis:')

#Programa Principal:

def teste():
    x = 8
    n = 9
    print(f'Na função "teste", "n" vale {n}.')
    print(f'Na função "teste", "x" vale {x}.')

n = 2
print(f'No programa principal, "n" vale {n}.')
teste()
#print(f'No programa principal, a variável "x" vale {x}.')
#Na linha acima, temos um problema. A variável "x" não pode ser utilizada fora da "def contador".
#Isso se deve ao fato de que "x" se trata de uma variável de escopo local, ou seja, ela só valerá para o local onde fora definida.

#No caso acima, "n" é uma variável de "escopo global", isso é, ela é usada em diferentes pontos do programa principal.
#Caso a variável n fosse declarada dentro de "def teste", o programa criaria uma variável a de escopo local.
#Ao passo de que manteria a variável a de escopo global. A seguir temos um exemplo para ilustrar o que fora dito:

def função():
    n1 = 4
    print(f'"n1" local (dentro) vale {n1}.')

n1 = 2
print(f'"n1" global (fora) vale: {n1}.')
função()

#A seguir, veremos uma maneira de tornar a variável "a" uma variável global em todos os locais onde ela for utilizada.

#Sem variável global:
def teste(b):
    a = 7
    b += 8
    c = 9
    print(f'Na função "teste", "a" vale {a}.')
    print(f'Na função "teste", "b" vale {b}.')
    print(f'Na função "teste", "c" vale {c}.')

a = 5
teste(a)
print(f'No programa principal, "a" vale {a}.')

#Com variável global:
def teste(b):
    global a
    a = 7
    b = 8
    c = 9
    print(f'Na função "teste", "a" vale {a}.')
    print(f'Na função "teste", "b" vale {b}.')
    print(f'Na função "teste", "c" vale {c}.')

a = 5
teste(a)
print(f'No programa principal, "a" vale {a}.')

print('Retornando Valores:')

#Para que um programa retorne valores, devemos usar o comando "return".

#Programa sem "return":
def somar(a = 0, b = 0, c = 0):
    s = a + b + c
    print(f'A soma dos valores digitados é igual a: {s}.')

somar(3, 2, 5)
somar(2, 2)
somar(6)

#Programa com "return":
def somar(a = 0, b = 0, c = 0):
    s = a + b + c
    return s
    #Agora, a variável resultado vai receber o valor de "s".

resultado_1 = somar(3, 2, 5)
resultado_2 = somar(2, 2)
resultado_3 = somar(6)
print(f'Os resultados obtidos foram: {resultado_1}, {resultado_2} e {resultado_3}.')
print(f'O resultado obtido foi: {somar(1, 2, 3)}.') #Outra maneira de se mostrar o resultado da função "somar".

print('Aplicação do Conteúdo Visto Até Aqui:')

def fatorial(num = 1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f

n = int(input('Digite um número para ver o seu fatorial: '))
print(fatorial(n))
print(f'O fatorial de {n} é: {fatorial(n)}.')
f1 = fatorial(6)
f2 = fatorial(4)
f3 = fatorial()
print(f'Os resultados obtidos foram: {f1}, {f2} e {f3}.')

def par_ou_ímpar(n = 0):
    if n % 2 == 0:
        return True
    else:
        return False

num = int(input('Digite um número para saber se ele é par ou ímpar: '))
print(par_ou_ímpar(num))
if par_ou_ímpar(num):
    print('É par.')
else:
    print('Não é par.')
    