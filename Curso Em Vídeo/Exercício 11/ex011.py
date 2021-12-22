print('Pintando Parede')
print()

largura = float(input('Digite a largura da parede: '))
altura = float(input('Digite a altura da parede: '))
área = largura * altura
tinta = área / 2
print(f'\nA sua parede tem uma dimensão de {largura:.2f} x {altura:.2f} e a sua área é de {área:.2f}m².')
print(f'\nPara pintar essa parede, você precisará de {tinta:.2f} litros de tinta.')
