print('Tratamento de Erros e Exceções')
print()

#Uma "exceção" é um erro semântico.
#Todo exceção, em Python, é filha de uma classe maior chamada "Exception".

#try: #Aqui vamos receber uma operação.

#except: #Aqui vamos receber uma exceção em caso de falha.

try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b

except:
    print('Infelizmente, tivemos um problema! :(')
    
else: #Aqui vamos receber o comando acerca do que fazer em caso de não haver exceção.
    print(f'O resultado é: {r:.1f}.')

finally: #Aqui vamos um comando que será executado independente de ter ocorrido um erro ou não.
    print('Volte sempre! Muito obrigado (a).')

try:
    c = int(input('Numerador: '))
    d = int(input('Denominador: '))
    r2 = c / d

except Exception as erro:
    #Se, ao lado de "except", adicionarmos a palavra "Exception", o erro detectado poderá ser mostrado ao usuário.
    #Para exibir o erro, devemos usar o como "as" e, após ele, definir uma variável que conterá o erro detectado.
    #Após a variável que conterá a exceção, devemos usar ponto e "class" + "underlines" para escolher o tipo do erro:

    print('Infelizmente, tivemos um problema! :(')
    print(f'A exceção (erro) detectada foi: {erro.__class__}.')

else: #Aqui vamos receber o comando acerca do que fazer em caso de não haver exceção.
    print(f'O resultado é: {r:.1f}.')

finally: #Aqui vamos um comando que será executado independente de ter ocorrido um erro ou não.
    print('Volte sempre! Muito obrigado (a).')

#É possível expandir a estrutura vista acima. Sendo assim, é possível se ter vários "try's" - para cada tipo de erro.

try:
    e = int(input('Numerador: '))
    f = int(input('Denominador: '))
    r3 = e / f

except (ValueError, TypeError): #Podemos abrir parênteses e adicionar vários tipos de erros.
    print('Tivemos um problema com os tipos de dados que você digitou.')

except ZeroDivisionError:
    print('Não é possível dividir um número por zero.')

except KeyboardInterrupt:
    print('O usuário preferiu não informar os dados solicitados.')

except Exception as erro:
    print(f'O erro encontrado foi: {erro.__cause__}.') #Além de "class", há outras opções para se selecionar aqui.

else:
    print(f'O resultado é: {r:.1f}.')

finally:
    print('Volte sempre! Muito obrigado (a).')
