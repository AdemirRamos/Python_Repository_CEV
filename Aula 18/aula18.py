print('Listas (Parte 2)')
print('')
teste = list()
teste.append('Gustavo')
teste.append(40)
print(teste)

teste = list()
teste.append('Gustavo')
teste.append(40)
galera = list()
galera.append(teste)
print(galera)
#Serão "printados" colchetes dentro de colchete pois é o caso de uma lista dentro de outra lista.


teste = list()
teste.append('Gustavo')
teste.append(40)
galera = list()
galera.append(teste)
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste)
print(galera)
#Nesse caso, o resultado será: "[['Maria', 22], ['Maria', 22]]". O método ".append()" gera uma conexão entra as listas, por isso tivemos o mesmo resultados 2 vezes.

teste = list()
teste.append('Gustavo')
teste.append(40)
galera = list()
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)
#O comando "[:]" quebra a conexão entre as listas, logo, o resultado será: "[['Gustavo', 40], ['Maria', 19]]". - Esse comando, também, gera uma cópia de uma lista.

galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
print(galera) #Resultado: será "printada" todo o conteúdo da lista "galera".
print(galera[0]) #Resultado: "['João, 19]".
print(galera[0][0]) #Resultado: "['João']".
print(galera[2][1]) #Resultado: "[13]".

galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
print(galera)
print(galera[0])
print(galera[0][0])
print(galera[2][1])
for p in galera:
    print(p)
#Resulado: forma uma lista com cada um dos elementos da lista logo abaixo o anterior.

galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
print(galera)
print(galera[0])
print(galera[0][0])
print(galera[2][1])
for p in galera:
    print(p[0])
#Resultado: aqui teremos apenas os nomes de "galera".

galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
print(galera)
print(galera[0])
print(galera[0][0])
print(galera[2][1])
for p in galera:
    print(p[1])
#Resultado: aqui teremos apenas as idades de "galera".

galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
print(galera)
print(galera[0])
print(galera[0][0])
print(galera[2][1])
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade.')
#Resultado: (Nome) tem (Idade) anos de idade. Exemplo prático (p[0] / p[1]): "João tem 19 anos de idade".

galera = list()
dado = list()
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:]) #Caso "[:]" não seja colocado, "dado.clear" vai gerar todas as listas vazias.
    dado.clear #Limpa a lista.
print(galera)
#Resulado: após as perguntas, todos os dados são armazenados em uma lista ("galera") e exibidos lado a lado.

galera = list()
dado = list()
total_maior_de_idade = total_menor_de_idade = 0
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear
for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        total_maior_de_idade += 1
    else:
        print(f'{p[0]} é menor de idade.')
        total_menor_de_idade += 1
print(f'Temos {total_maior_de_idade} maiores de idade e {total_menor_de_idade} menores de idade.')
#Resultado: Serão apresentadas as perguntas relativas a nome e idade e, após isso, serão escritos os "prints" com os dados informados.
