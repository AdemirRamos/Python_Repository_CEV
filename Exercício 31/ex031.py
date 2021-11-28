print('Custo Da Viagem')
print()
distan = float(input('Digite a distância da sua viagem: '))
preço1 = 0.50 * distan
preço2 = 0.45 * distan
if distan <= 200:
    print('Você está preste a começar uma viagem de {}km.'.format(distan))
    print('O preço dessa viagem será de: R${:.2f}.'.format(preço1))
else:
    print('A sua viagem tem uma distância maior do que 200km.')
    print('O preço da sua viagem será de: R${:.2f}.'.format(preço2))

#As linhas acima representam a maneira como eu resolvi o exercício. A seguir, está a maneira como o Guanabara resolveu:

distância = float(input('Qual é a distância da sua viagem? '))
print('Você está prestes a começar uma viagem de {}km.'.format(distância))
if distância <= 200:
    print = distância * 0.50
else:
    print = distância * 0.45
preço = distância * 0.50 if distância <= 200 else distância * 0.45
print('E o preço da sua passagem será de: {:.2f}.'.format(preço))

#A segunda maneira de se resolver o problema envolve a condição simplificada.