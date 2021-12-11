print('Um Print Especial')
print()
def linha(string_1):
    tamanho = len(string_1)
    linha = tamanho * '~' * 3
    print(linha)

def linha_2(string_2):
    tamanho_2 = len(string_2)
    linha_2 = tamanho_2 * '~' * 4
    print(linha_2)
    
def linha_3(string_3):
    tamanho_3 = len(string_3)
    linha_3 = tamanho_3 * '~' * 3
    print(linha_3)

string_1 = str(print('Ademir Ramos'))
linha(string_1)
print()
string_2 = str(print('Curso de Python'))
linha_2(string_2)
print()
string_3 = str(print('Exercício 97'))
linha_3(string_3)

#Resolução do Guanabara:

print('Um Print Especial')
print()

def escreva(message):
    tamanho = len(message) + 4
    print('~' * tamanho )
    print(f'  {message}')
    print('~' * tamanho)
    
escreva('Gustavo Guanabara.')
escreva('Curso de Python no YouTube.')
escreva('CEV.')
