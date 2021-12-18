print('Finalizando o Projeto - Ex115C')
print()

#Módulo / Pacote da Aula 115A:

def linha(tamanho = 50):
    return '-' * tamanho

def cabeçalho(text):
    print(linha())
    print(text.center(50))
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

#Módulo / Pacote da Aula 115A

#Módulo / Pacote da Aula 115B:

def arquivo_existe(nome):
    try:
        a = open(nome, 'rt') #Essa função tenta abrir o arquivo. / "rt" == "read text". Faz a leitura do arquivo (do tipo "txt").
        a.close() #Fecha o arquivo.
        
    except FileNotFoundError:
        return False

    else:
        return True

def criar_arquivo(nome):
    try:
        a = open(nome, 'wt+')
        #Essa função tenta abrir o arquivo. / "wt+" == "write text". Cria um arquivo (do tipo "txt") - o "+" é o responsávle pela criação do arquivo.
        a.close()

    except:
        print('\033[31mHouve um erro ao se criar o arquivo.\033[m')

    else:
        print(f'Arquivo {nome} criado com sucesso.'.center(50))

def ler_arquivo(nome):
    try:
        a = open(nome, 'rt')

    except:
        print('\033[31mErro ao ler o arquivo.\033[m')

    else:
        cabeçalho('Pessoa (s) Cadastrada (s)')
        #print(a.read()) #Esse comando faz com que a leitura do arquivo seja feita. O comando também poderia ser ".readlines()".
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
        
    finally:
        a.close()
    
#Módulo / Pacote da Aula 115B

#Módulo / Pacote da Aula 115C

def cadastrar(file, nome = 'desconhecido', idade = 0):
    try:
        a = open(arquivo, 'at')
        #O "'a'" de "open" significa "append" e serve para adicionar informações no arquivo.
        #"'at'" adiciona um novo texto ao arquivo.capitalize

    except:
        print('Houve um erro ao se abrir o arquivo.')

    else:
        try:
            a.write(f'{nome};{idade}\n') #Esse comando (".write()") nos permite escrever algo dentro do arquivo.

        #É possível se ter um "try" dentro de outro "try".

        except:
            print('Houve um erro ao se escrever os novos dados no arquivo.')

        else:
            print(f'Novo registro ({nome}) adicionado.')
            a.close()
        
#Módulo / Pacote da Aula 115C

linha()
cabeçalho('Sistema Arquivo (v1.0)'.center(50))

from time import sleep

arquivo = 'Curso_Em_Vídeo.txt'

if arquivo_existe(arquivo):
    print('Arquivo encontrado com sucesso.'.center(50))
else:
    print('Arquivo não encontrado.'.center(50))
    criar_arquivo(arquivo)

while True:
    resposta = menu(['Ver Pessoas Cadastradas', 'Cadastrar Nova (s) Pessoa (s)', 'Sair do Programa'])
    if resposta == 1:
        cabeçalho('Opção 1')

        #Opção de listar o conteúdo de um arquivo:

        ler_arquivo(arquivo)
        
    elif resposta == 2:

        #Opção de cadastrar uma ou mais pessoas.

        cabeçalho('Novo Cadastro')
        
        nome = str(input('Nome: '))
        idade = leia_int('Idade: ')
        cadastrar(arquivo, nome, idade)
                
    elif resposta == 3:

        #Opção de sair do sistema.
        
        cabeçalho('Saindo do sistema... até logo!')
        break
    
    else:

        #Opção para caso o usuário digite uma opção incorreta / inválida no menu.
        
        print('\033[31mErro! Digite uma opção válida\033[m')
    sleep(1)

#Arquivo com os nomes das pessoas cadastradas

'''Gustavo;41
Ana;22
Pedro;35
Paulo;95
José;55'''

#A partir da adição do método de cadastro, esse arquivo com os nomes das pessoas cadastradas pode ser deletado.

#Arquivo com os nomes das pessoas cadastradas
