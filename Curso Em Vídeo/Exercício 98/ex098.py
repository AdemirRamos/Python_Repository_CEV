print('Função de Contador')
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

#Resolução do Guanabara:

print('Função de Contador')
print()

from time import sleep

def contador(i, f, p):

    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    
    print('-=' * 20)
    print(f'Contagem de {i} até {f} de {p} em {p}.')
    sleep(2.5)
        
    if i < f:
        contador = i
        while contador <= f:
            print(f'{contador}', end=' ')
            sleep(0.5)
            contador += p
        print('Fim!')
    else:
        contador = i
        while contador >= f:
            print(f'{contador}', end=' ')
            #A depender da versão do PyCharm, pode ocorrer um erro ao se usar o "sleep".
            #Para se evitar esse erro (caso ele aconteça), basta adicionar, após "end=''", o seguinte comando: "flush = True".
            sleep(0.5)
            contador -= p
        print('Fim!')
    
contador(0, 100, 10)
contador(10, 0, 2)
print('-=' * 20)
print('Agora e a sua vez de personalizar a contagem!')
início = int(input('Ínicio: '))
fim = int(input('Fim:       '))
passo = int(input('Passo:   '))
contador(início, fim, passo)