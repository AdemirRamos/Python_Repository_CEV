print('Transformando Módulos Em Pacotes')
print()

from utilidadescev import moeda

p = float(input('Digite um preço: R$'))
moeda.resumo(p)
