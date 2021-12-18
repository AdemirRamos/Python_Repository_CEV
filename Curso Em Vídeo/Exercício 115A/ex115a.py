print('Criando Um Menu Em Python - Ex115A')
print()

#Módulo: Menu

def menu():
    from time import sleep
    while True:
        título = 'Menu Principal'
        print('=' * 40)
        print(f'{título:^40}')
        print('=' * 40)
        print()
        print('=' * 40)
        option_1 = '\033[1;34m1\033[m - \033[1;34mVer pessoas cadastradas\033[m'
        sleep(1)
        print(f'{option_1:<40}')
        option_2 = '\033[1;34m2\033[m - \033[1;34mCadastrar nova (s) pessoa (s)\033[m'
        sleep(1)
        print(f'{option_2:<40}')
        option_3 = '\033[1;34m3\033[m - \033[1;34mSair do programa\033[m'
        sleep(1)
        print(f'{option_3:<40}')
        print('=' * 40)
        print()
        sleep(1)
        opção = int(input('Selecione uma opção: '))
        print()
        if opção == 1:
            sleep(1)
            print('=' * 40)
            string_1 = 'Opção 1'
            print(f'{string_1:^40}')
            print('=' * 40)
            print()
        elif opção == 2:
            sleep(1)
            print('=' * 40)
            string_2 = 'Opção 2'
            print(f'{string_2:^40}')
            print('=' * 40)
            print()
        elif opção == 3:
            sleep(1)
            break

#Módulo: Menu

menu()
print('Fim do programa.')

#import *: Importa todos os arquivos do módulo / pacote.

#Resolução do Guanabara:

print('Criando Um Menu Em Python - Ex115A')
print()

def linha(tamanho = 42):
    return '-' * tamanho

def cabeçalho(text):
    print(linha())
    print(text.center(42))
    print(linha())

def menu(lista):
    cabeçalho('Menu Principal')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print(linha())
    opção = leia_int('\033[32mSua opção: \033[m')
    return opção
    
def leia_int(message):
    while True:
        try:
            n = int(input(message))

        except (ValueError, TypeError):
            print('\033[31mErro! Por favor, digite um número inteiro válido.\033[m')
            continue
        
        except(KeyboardInterrupt):
            print('\033[31mEntrada de dados interrompida pelo usuário.\033[m')
            return 0
                
        else:
            return n
    
linha()
cabeçalho('Sistema Arquivo (v1.0)')

from time import sleep

while True:
    resposta = menu(['Ver Pessoas Cadastradas', 'Cadastrar Nova (s) Pessoa (s)', 'Sair do Programa'])
    if resposta == 1:
        cabeçalho('Opção 1')
    elif resposta == 2:
        cabeçalho('Opção 2')
    elif resposta == 3:
        cabeçalho('Saindo do sistema... até logo!')
        break
    else:
        print('\033[31mErro! Digite uma opção válida\033[m')
    sleep(1)
