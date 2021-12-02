print('Índice De Massa Corporal')
print()
peso = float(input('Digite o seu peso (em KG): '))
altura = float(input('Digite a sua altura (em M): '))
imc = peso / (altura ** 2)
if imc < 18.5:
    print('O seu IMC é de: {:.1}. Você está abaixo do peso normal.'.format(imc))
elif imc > 18.5 and imc < 25:
    print('O seu IMC é de: {:.1f}. Você está no peso ideal.'.format(imc))
elif imc > 25 and imc < 30:
    print('O seu IMC é de: {:.1f}. Você está com sobrepeso.'.format(imc))
elif imc > 30 and imc < 40:
    print('O seu IMC é de: {:.1f}. Você está com obesidade.'.format(imc))
elif imc > 40:
    print('O seu IMC é de: {:.1f}. Você está com obesidade mórbida.'.format(imc))
