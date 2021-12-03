print('Exercício 98')
print()

def um(valor):
    print('Realizando a contagem com passo 1.')
    valor = 1
    for valor in range(1, 11):
        print(f'{valor}', end=' ')
        valor += 1

def dois(valor):
    print('Realizando a contagem com passo 2.')
    valor = 0
    for valor in range(0, 11, 2):
        print(f'{valor}', end=' ')
        valor += 2

def your_count(valor):
        for valor in range(begin, end + 1, step):
            print(f'{valor}', end=' ')
            valor += step
    
um(1)
print()
print()

dois(1)
print()
print()

begin = int(input('Digite o ínicio da contagem: '))
end = int(input('Digite o fim da contagem: '))
step = int(input('Digite o passo da contagem: '))
your_count(step)
