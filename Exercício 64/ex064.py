print('Tratando Vários Valores (Versão 1.0)')
print('')
num = int(input('Digite o número [999 para parar]: '))
cont = 0
números = 0
while num != 999:
    cont += num
    números += 1
    soma = cont + num - num
    num = int(input('Digite o número [999 para parar]: '))
print('A soma de todos os valores que você digitou (menos 999) é igual a: {}.'.format(soma))
print('E, ao todo, você digitou {} números.'.format(números))

#A seguir, a maneira como o Guanabara resolveu o exercício:

print('')
núm = cont = soma = 0
while núm != 999:
    núm = int(input('Digite um número [999 para parar]:'))
    soma += núm
    cont += 1
#Abaixo vai uma maneira de se resolver o problema:
#Na aula, entretanto, o Guanabara usou uma resolução igual à minha.
print('Você digitou {} números e a soma entre eles foi {}.'.format(cont - 1, soma - 999))
