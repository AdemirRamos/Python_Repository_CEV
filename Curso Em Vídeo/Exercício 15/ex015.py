print('Aluguel de Carros')
print()

dias = int(input('Por quantos dias o carro vai ser alugado? Digite aqui: '))
km = float(input('Quantos km foram rodados? Digite aqui: '))
aluguel = dias * 60 + km * 0.15
print(f'\nO valor do aluguel do carro vai custar: R${aluguel:.2f}.')

#O aluguel também poderia ser escrito assim: "aluguel = (dias * 60) + (km * 0.15)".
