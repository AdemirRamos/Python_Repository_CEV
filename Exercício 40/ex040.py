print('Média')
print()
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
if m >= 7.0:
    print('Parabéns! A sua média é: {:.1f}. Você está aprovado!'.format(m))
elif m > 5.0 and m < 6.9:
    print('A sua média é: {:.1f}. Você está de recuperação.'.format(m))
elif m < 5.0:
    print('A sua média é {:.1f}. Você está reprovado.'.format(m))
