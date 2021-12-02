print('Analisador de Textos')
print()

'''frase = ('Curso Em Vídeo Python')
print(frase[1:18])'''

nome = str(input('Digite o seu nome: ')).strip()
print('')
print('O seu nome, em letras maiúsculas, fica assim: {}.'.format(nome.upper()))
print('O seu nome, em letras minúsculas, fica assim: {}.'.format(nome.lower()))
print('O total de letras em seu nome é de: {} letras.'.format(len(nome) - nome.count(' ')))
print('O seu primeiro nome tem um total de {} letras.'.format(nome.find(' ')))
separa = nome.split()
print('O seu primeiro nome é: {} e ele tem {} letras.'.format(separa[0], len(separa[0])))
print('')

#Comentário: é importante salientar que em "nome.count(' ')" é preciso se colocar um espaço entre aspas
#(caso contrário), teremos um erro. Mais uma coisa: a barra entre len(nome) e nome.count é um sinal de menos.
#Também há um espaço em "nome.find(' ')"