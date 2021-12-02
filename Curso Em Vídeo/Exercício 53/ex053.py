print('Detector de Palíndromo')
print()
frase = str(input('Digite algum nome ou frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
#outra opção para se formar o palíndromo: inverso = junto[::-1]
for letra in range(len(junto) - 1, - 1, -1):
    inverso += junto[letra]
print('O inverso de {} é: {}.'.format(junto, inverso))
if inverso == junto:
    print('Essa palavra ou frase forma um palíndromo.')
else:
    print('Essa palavra ou frase não forma um palíndromo.')
