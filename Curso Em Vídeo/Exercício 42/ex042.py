print('Analisando Triângulos (Versão 2.0)')
print()
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima podem formar um triângulo.')
    if r1 == r2 == r3:
        print('A soma entre esses segmentos forma um triângulo equilátero.')
    elif r1 != r2 != r3 != r1:
        print('A some entre esses segmentos forma um triângulo escaleno.')
    else:
        print('A soma entre os segmentos forma um triângulo isóceles.')
else:
    print('A some entre esses segmentos não forma um triângulo.')
