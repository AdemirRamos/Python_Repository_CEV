print('Módulos e Pacotes')
print()

# - Modularização é o ato de cronstruir módulos.

# - O foco da modularização é dividir um programa grande em partes menores. Também tem como foco aumentar a legibilidade de um programa.

# - A modularização também torna o seu programa mais enxuto e simples.

# - Uma das vantagens da modularização consiste na manutenção de sistema / programa.

#Parte Prática da Aula:

def fatorial(n):
    f = 1
    for c in range(1, n + 1):
        f *= c
    return f

def dobro(n):
    return n * 2

def triplo(n):
    return n * 3

#É preciso pegar todas essas funções (acima) e colocá-las dentro de um novo arquivo para se gerar um novo módulo.
#Ao criar um módulo, ele, por definição, não estará conectado ao seu arquivo-proveniente.
#Para sanar esse problema, basta importar o módulo da mesma maneira que se importa bibliotecas.
#Exemplo: "import [nome do arquivo onde está (ão) o (s) módulo (s)]" ou "from [nome do arquivo] import [nome (s) da (s) função (ões)]".
#Exemplo prático para a segunda maneira de se importar: from A import B, C, D

#A segunda maneira de importação ("from [nome do módulo/biblioteca] import [nome da {s} função {ões}]") não é recomendada pelo Python.
#Isso se deve ao fato de que, em diferentes módulos/bibliotecas, pode ser possível achar funções com o mesmo nome.
#Em sendo esse o caso, o Python, talvez, não saiba exatamente qual função de qual módulo/biblioteca você deseja importar.
#Caso dois módulos/bibliotecas importados possuam, ambos, uma função com o mesmo nome, por definição, o Python importará a função do último módulo importado.

#P. S.: Desde que tenha funções internas, todo arquivo terminado com ".py", para o Python, é considerado um módulo.

num = int(input('Digite um valor: '))
fat = fatorial(num)
print(f'O fatorial de {num} é {fat}.')
print(f'O dobro de {num} é {dobro(num)}.')
print(f'O tripo de {num} é {triplo(num)}.')

#Algumas vantagens da modularização:

# - Organização do código;
# - Facilidade na manutenção;
# - Ocultação do código detalhado;
# - Reutilização em outros projetos.

#Caso nem os módulos sejam suficiente para o que você deseja fazer, você pode recorrer aos "pacotes".

#P. S.: Em outras linguagens de programação, os "pacotes" são chamados de "biblioteca".

#Exemplo prático (sobre pacotes):

#Pacotes são módulos é a junção de módulos separados por assuntos. Portanto, o "pacote" nada mais é do que uma pasta que contem módulos.
#Dentro de pacotes, você pode separar as suas funções por assunto. Exemplo: funções para "strings"; funções para números; e assim por diante.
#Sendo assim, também é possível importar, de dentro de um pacote, um módulo específico.

#Exmplo: "import A"; "from A import ABC".

#Dentro de um projeto Python, toda pasta é considerada um pacote. Para se criar módulos dentro de um pacote, basta criar pastas para estes módulos.

#Existe uma sintaxe para nomes de arquivos dentro de pacotes: "__init___.py".
