print('Primeira e Última Ocorrência De Uma String')
print()
frase = str(input('Digite uma frase: ')).upper().strip()
print('')
print('A letra "A" aparece {} vezes.'.format(frase.count('A')))

#De novo, é possível se usar tanto ".upper" quanto ".lower".

print('A letra "A" aparece pela primeira vez na posição {}.'.format(frase.find('A')+1))
print('A letra "A" aparece pela última vez na posição {}.'.format(frase.rfind('A')+1))
