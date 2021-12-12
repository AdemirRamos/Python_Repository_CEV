print('Função Para Fatorial')
print()

def fatorial(n, show = False):
    print()
    
    """

    A função "fatorial" calcula o fatorial do número escolhido pelo usuário.

    - parâmetro n: representa o número escolhido para ter o seu fatorial apresentado;
    - parâmetro show: se receber "True", mostrará o cálculo do fatorial do número escolhido pelo usuário; se "False", não mostrará o cálculo;
    - return: retorna o resultado final da função fatorial para o parâmetro da chamada da função.

    """
    
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f

print(fatorial(5, False)) #Também poderia ser "show = True". / #O segundo parâmetro é opcional. Se "True", ,mostrará o cálculo; se "False", não mostrará.
help(fatorial)
