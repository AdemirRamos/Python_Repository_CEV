print('Aumentos Múltiplos')
print()
sal = float(input('Digite o salário do funcionário: R$'))
sal15 = sal + (sal * 15 / 100)
sal10 = sal + (sal * 10 / 100)
if sal <= 1250:
    print('O seu salário sofrerá um reajuste de 15%. \nAgora, o seu salário será de R${:.2f}.'.format(sal15))
if sal > 1250:
    print('O seu salário sofrerá um reajuste de 10%. \nAgora, o seu salário será de R${:.2f}.'.format(sal10))
print()

#Vamos ao modo como o Guanabara resolveu o exercício.

salário = float(input('Digite o salário do funcionário: R$'))
if salário <= 1250:
    novo = salário + (salário * 15 / 100)
else:
    novo = salário + (salário * 10 / 100)
print('Quem ganhava R${:.2f} vai passar a ganhar R${:.2f}.'.format(salário, novo))
