print('Calculando Descontos')
print()

preço = float(input('Digite o preço do produto: R$'))
off = preço * 5 / 100
print(f'\nO produto que custa R${preço:.2f}, com um desconto de 5%, passa a custar R${preço - off:.2f}.')

#Outra maneira de escrever o desconto: "off = preço - (preço * 5 / 100)
