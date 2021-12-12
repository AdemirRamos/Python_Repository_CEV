print('Sistema de Ajuda Interativo em Python')
print()

from time import sleep

c = ('\033[m', '\033[0;30;41m', '\033[0;30;42m', '\033[0;30;43m', '\033[0;30;44m', '\033[0;30;45m', '\033[7;30m')

#1ª cor: sem cor; 2ª cor: vermelhor; 3ª cor: verde; 4ª cor: amarelo; 5ª cor: azul; 6ª cor: roxo; 7ª cor: branco.

def ajuda(command):
    título(f'Acessando o manual do comando \'{c}\'', 4)
    print(c[6], end='')
    help(command)
    print(c[0], end='')
    sleep(2)

def título(message, cor = 0):
    tamanho = len(message) + 4
    print(c[cor], end='')
    print('~' * tamanho)
    print(f'  {message}')
    print('~' * tamanho)
    print(c[0], end='')
    sleep(1)
    
comando = ''
while True:
    título('Sistema de Ajuda Interativo PyHelp', 2)
    comando = str(input('Função da Biblioteca: '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
        
título('Terminamos por aqui! Muito obrigado! Volte sempre!', 1)
título('Até logo!', 1)
