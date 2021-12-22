
print('Conversor de Temperaturas')
print()

tef = float(input('Digite a temperatura em ºF: '))
conversão = (tef - 32) * 5 / 9
print('\nTemperatura: {:.1f}ºF.'.format(conversão))
print()
tec = float(input('Digite a temperatura em ºC: '))
conver = (tec * 9 / 5) + 32
print('\nConversão: {:.1f}ºC'.format(conver))
