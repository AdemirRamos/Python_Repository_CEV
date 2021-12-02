print('Radar Eletrônico')
print()
velocidade = float(input('Qual é a velocidade atual do carro? '))
if velocidade > 80:
    print('VOCÊ FOI MULTADO! Você excedeu o limite de velocidade que é de 80km/h.')
    multa = (velocidade - 80) * 7
    print('O valor da multa que você deve pagar é de: R${:.2f}.'.format(multa))
print('Tenha um bom dia e dirija com segurança!')
