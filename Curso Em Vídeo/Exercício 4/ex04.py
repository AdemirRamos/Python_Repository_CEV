print('Dissecando Uma Variável')
print()

something = input('Digite Algo: ')
print()
print(f'O que foi digitado pertence ao tipo: {type(something)}.')
print(f'O que foi digitado só possui espaços? {something.isspace()}.')
print(f'O que foi digitado é um número? {something.isnumeric()}.')
print(f'O que foi digitado é alfabético? {something.isalpha()}.')
print(f'O que foi digitado é alfanumérico? {something.isalnum()}.')
print(f'O que foi digitado é maiúsculo? {something.isupper()}.')
print(f'O que foi digitado é minúsculo? {something.islower()}.')
print(f'O que foi digitado está capitalizado? {something.istitle()}.')

#Em Python, todo Objeto possui características e realiza funcionalidades; todo Objeto possui atributos e métodos.
#Em Python, variáveis são Objetos. 
