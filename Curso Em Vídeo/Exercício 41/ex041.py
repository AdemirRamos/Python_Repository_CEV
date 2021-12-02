print('Classificando Atletas')
print()
from datetime import date
ano = date.today().year
nascimento = int(input('Digite o ano no qual você nasceu: '))
idade = ano - nascimento
if idade <= 9:
    print('De acordo com a sua idade ({:.0f} anos), você pertence à categoria "Mirim".'.format(idade))
elif idade <= 14:
    print('De acordo com a sua idade ({:.0f} anos), você pertence à categoria "Infantil".'.format(idade))
elif idade <= 19:
    print('De acordo com a sua idade ({:.0f} anos), você pertence à categoria "Junior".'.format(idade))
elif idade <= 25:
    print('De acordo com a sua idade ({:.0f} anos), você pertence à categoria "Sênior".'.format(idade))
elif idade > 25:
    print('De acordo com a sua idade ({:.0f} anos), você pertence à categoria "Master".'.format(idade))
