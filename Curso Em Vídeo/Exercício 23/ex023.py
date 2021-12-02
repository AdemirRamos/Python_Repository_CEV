print('Separando Dígitos De Um Número')
print()
num = int(input('Digite algum número: '))
n = str(num)
print('Analisando o número {}...'.format(num))
print('Unidade: {};'.format(n[3]))
print('Dezena: {};'.format(n[2]))
print('Centena: {};'.format(n[1]))
print('Milhar: {}.'.format(n[0]))
print('')
num = (int(input('Digite algum número: ')))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Unidade: {};'.format(u))
print('Dezena: {};'.format(d))
print('Centena: {};'.format(c))
print('Milhar: {}.'.format(m))

#Use a segunda forma caso o seu número não tenha milhar e/ou centena.
