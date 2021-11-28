print('Simulador De Caixa Eletrônico')
print('')
print('=' * 30)
print('{:^30}'.format('Banco CEV'))
print('=' * 30)
print('')
valor = int(input('Quanto dinheiro você deseja sacar? R$'))
print('')
total = valor
cédula = 50
total_de_cédulas = 0
while True:
    if total >= cédula:
        total -= cédula
        total_de_cédulas += 1
    else:
        if total_de_cédulas > 0:
            print(f'Total (de cédulas retiradas): {total_de_cédulas} cédulas de R${cédula:.2f}.')
        if cédula == 50:
            cédula = 20
        elif cédula == 20:
            cédula = 10
        elif cédula == 10:
            cédula = 1
        total_de_cédulas = 0
        if total == 0:
            break
print('')
print('Volte sempre ao Banco CEV! Tenha um bom dia!')
