print('Verificando As Primeiras Letras De Um Texto')
print()
cidade = str(input('Digite o nome da cidade na qual você nasceu: ')).strip()
print(cidade[:5].upper() == 'SANTO')
#Se usa o ".upper" para o computador entender "santo" (independente de como "santo" seja escrita.)
#Ao invés de ".upper", também poderia ser ".lower": print(cidade[:5].lower() == 'santo')
