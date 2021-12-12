def resumo(a, b, c):
    texto = 'Resumo do Valor'
    print('~' * 20)
    print(f'{texto:^19}')
    print('~' * 20)
    print()
    print('~' * 35)
    print(f'Preço analisado: {a:>14}')
    
    dobro = a * 2
    print(f'Dobro do valor analisado: {dobro:>5}')
    
    metade = a / 2
    print(f'Metade do valor analisado: {metade:>5}')

    vinte = (a * 20 / 100)
    increase = vinte + a
    print(f'20% de aumento: {increase:>16}')

    doze = (a * 12 / 100)
    redução = a - doze
    print(f'12% de redução: {redução:>16.1f}')
    print('~' * 35)
