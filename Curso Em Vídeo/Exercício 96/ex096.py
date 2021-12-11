print('Função Para Calcular a Área')
print()
def cálculo(altura, largura):
    área = altura * largura
    print(f'A altura de {altura} vezes a largura de {largura} gera uma área de {área}m2.')

altura = float(input('Digite a altura: '))
largura = float(input('Digite a largura: '))
cálculo(altura, largura)

#Resolução do Guanabara:

print('Função Que Calcula Área')
print()

def área(largura, comprimento):
    a = largura * comprimento
    print(f'A área de um terreno {largura} x {comprimento} é igual a {a}m².')

print('Controle de terrenos.')
print('-' * 20)
l = float(input('Largura (m): '))
c = float(input('Comprimento (m): '))
área(l, c)
