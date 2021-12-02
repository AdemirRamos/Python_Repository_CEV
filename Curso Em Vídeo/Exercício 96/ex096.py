print('Função Para Calcular a Área')
print()
def cálculo(altura, largura):
    área = altura * largura
    print(f'A altura de {altura} vezes a largura de {largura} gera uma área de {área}m2.')

altura = float(input('Digite a altura: '))
largura = float(input('Digite a largura: '))
cálculo(altura, largura)
