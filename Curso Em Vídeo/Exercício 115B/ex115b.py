print('Arquivos Com Python - Ex115B')
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
        print(a.readlines()) #Esse comando faz com que a leitura do arquivo seja feita. O comando também pode ser ".read()".

#Módulo / Pacote da Aula 115B

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
        cabeçalho('Opção 2')
    elif resposta == 3:
        cabeçalho('Saindo do sistema... até logo!')
        break
    else:
        print('\033[31mErro! Digite uma opção válida\033[m')
    sleep(1)

#Arquivo com os nomes das pessoas cadastradas

'''Gustavo;41
Ana;22
Pedro;35
Paulo;95
José;55'''

#Arquivo com os nomes das pessoas cadastradas
