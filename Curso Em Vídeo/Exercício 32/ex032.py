print('Ano Bissexto')
print()
from datetime import date
ano = int(input('Qual anos você gostaria de analisar (digite 0 para ver o ano atual): '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('Este ano ({}) é bissexto.'.format(ano))
else:
    print('Este ano ({}) não é bissexto.'.format(ano))
