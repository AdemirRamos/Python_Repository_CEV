print('Módulo Value')
print()

def valor(value):
    half = value / 2
    double = value * 2
    ten = (value * 10 / 100)
    total = ten + value
    print()
    print(f'A metade do valor digitado é: R${half:.2f};')
    print(f'O dobro do valor digitado é: R${double:.2f};')
    print(f'Um aumento de 10% em cima do valor digitado é igual a: {total:.2f}.')
