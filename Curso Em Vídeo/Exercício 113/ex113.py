print('Funções Aprofundadas Em Python')
print()

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

def leia_float(message):
    while True:
        try:
            n = float(input(message))
            
        except (ValueError, TypeError):
            print('\033[31mErro! Por favor, digite um número real válido.\033[m')
            continue
            
        except (KeyboardInterrupt):
            print('\033[31mEntrada de dados interrompida pelo usuário\033[m')
            return 0
            
        else:
            return n

inteiro = int(input('Digite um número inteiro: '))
real = float(input('Digite um número real: '))
print(f'O valor inteiro digitado foi {inteiro}; o valor real digitado foi: {real}.')
