print('Grupo Da Maior Idade')
print()
from datetime import date
ano = date.today().year
totmaior = 0
totmenor = 0
for n in range(1, 8):
    idade1 = int(input('Digite o ano de nascimento da {}ª: '.format(n)))
    idade2 = ano - idade1
    if idade2 >= 18:
        totmaior += 1
    else:
        totmenor += 1
print('Ao todo, tivemos {} pessoa (s) menor (es) de idade.'.format(totmenor))
print('E também tivemos {} pessoa (s) maior (es) de idade.'.format(totmaior))
