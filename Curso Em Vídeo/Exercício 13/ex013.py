print('Reajuste Salarial')
print()

salário = float(input('Qual é o salário do funcionário: R$'))
increase = salário + (salário * 15 / 100)
print(f'\nO salário do funcionário, após um reajuste de 15%, será igual a: R${increase:.2f}.')
