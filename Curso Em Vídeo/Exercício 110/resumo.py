def string():
    texto = 'Resumo do Valor'
    print('~' * 20)
    print(f'{texto:^19}')
    print('~' * 20)
    print()
    print('~' * 35)

def math(a, b, c):
    print(f'Preço analisado:           R${a:>5}')
    
    dobro = a * 2
    print(f'Dobro do valor analisado:  R${dobro:>5}')
    
    metade = a / 2
    print(f'Metade do valor analisado: R${metade:>5}')

    vinte = (a * 20 / 100)
    increase = vinte + a
    print(f'20% de aumento:            R${increase:>5}')

    doze = (a * 12 / 100)
    redução = a - doze
    print(f'12% de redução:            R${redução:>5.1f}')
    print('~' * 35)
