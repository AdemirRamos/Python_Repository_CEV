print('Conversor de Medidas')
print()

medida = float(input('Digite uma distância em metros: '))
print(f'\nA medida de {medida}m², corresponde a: ', end=' ')
print(f'{medida / 1000:.0f}km; {medida / 100}hm; {medida / 10}dam; {medida * 10:.0f}dm; {medida * 100:.0f}cm; {medida * 1000:.0f}mm.')
