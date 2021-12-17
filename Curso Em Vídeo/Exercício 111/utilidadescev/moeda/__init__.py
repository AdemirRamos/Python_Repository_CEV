def aumentar(preço = 0, taxa = 0, formato = False):
    res = preço * (preço * taxa / 100)
    return res if formato is False else moeda(res)

def diminuir(preço = 0, taxa = 0, formato = False):
    res = preço - (preço * taxa / 100)
    return res if formato is False else moeda(res)

def dobro(preço = 0, formato = False):
    res = preço * 2
    return res if not formato else moeda(res)

def metade(preço = 0, formato = False):
    res = preço / 2
    return res if not formato else moeda(res)

def moeda(preço = 0, moeda = 'R$'):
    return f'{moeda}{preço:.2f}'.replace('.', ',')

def resumo(preço = 0, taxa = 10, redução = 5):
    print('=' * 35)
    print('Resumo do Valor'.center(35))
    print('=' * 35)
    print(f'Preço analisado: \t{moeda(preço)}')
    print(f'Dobro do preço: \t{dobro(preço, True)}')
    print(f'Metade do preço: \t{metade(preço, True)}')
    print(f'Com {taxa}% de aumento: \t{aumentar(preço, taxa, True)}')
    print(f'Com {redução}% de redução: \t{diminuir(preço, redução, True)}')
    print('=' * 35)

