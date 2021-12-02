print('Comparando Números')
print()
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
if num1 > num2:
    print('O primeiro número ({}) é maior que o segundo ({}).'.format(num1, num2))
elif num2 > num1:
    print('O segundo número ({}) é maior do que o primeiro ({}).'.format(num2, num1))
elif num1 == num2:
    print('Os dois números são iguais (em grandeza).')
