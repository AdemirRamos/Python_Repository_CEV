print('Dicionários')
print()

pessoa = {'nome': 'Gustavo', 'sexo': 'Masculino', 'idade': 22}
print(pessoa) #Resultado: "{'nome': 'Gustavo', 'sexo': 'Masculino', 'idade': 22}"
print(pessoa['nome']) #Resultado: "Gustavo".
print(pessoa['idade']) #Resultado: 22
print(f'O {pessoa["nome"]} tem {pessoa["idade"]} anos de idade.') #Resultado: "O Gustavo tem 22 anos de idade".
print(pessoa.keys()) #Resultado: "dict_keys(['nome', 'sexo', 'idade'])".
print(pessoa.values()) #Resultado: "dict_keys(['Gustavo', 'Masculino', 22])".
print(pessoa.items()) #Resultado: "dict_items([('nome', 'Gustavo'), ('sexo', 'Masculino'), ('idade': 22)])". Uma Lista com três Tuplas.

for k in pessoa.keys():
    print(k) #Resultado: "nome", "sexo", "idade".
for k in pessoa.values():
    print(k) #Resultado: "Gustavo", "Masculino", "22".
for k, v in pessoa.items():
    print(f'{k} = {v}') #Resultado: "nome = Gustavo", "sexo = Masculino", "idade = 22".

pessoa = {'nome': 'Gustavo', 'sexo': 'Masculino', 'idade': 22}
del pessoa['sexo']
print(pessoa)
for k, v in pessoa.items():
    print(f'{k} = {v}') #Resultado: "nome = Gustavo", "idade = 22".

pessoa = {'nome': 'Gustavo', 'sexo': 'Masculino', 'idade': 22}
pessoa['nome'] = 'Leandro'
print(pessoa)
for k, v in pessoa.items():
    print(f'{k} = {v}') #Resultado: "nome = Leandro", "sexo = Masculino", "idade = 22".

pessoa = {'nome': 'Gustavo', 'sexo': 'Masculino', 'idade': 22}
pessoa['peso'] = 98.5
print(pessoa)
for k, v in pessoa.items():
    print(f'{k} = {v}') #Resultado: "nome = Leandro", "sexo = Masculino", "idade = 22", "peso = 98.5".

brasil = []
estado_1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado_2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado_1)
brasil.append(estado_2)
print(estado_1) #Resultado: "{'uf': 'Rio de Janeiro', 'sigla': 'RJ'}".
print(estado_2) #Resultado: "{'uf': 'São Paulo', 'sigla': 'SP'}".
print(brasil) #Resultado: "[{'uf': 'Rio de Janeiro', 'sigla': 'RJ'}, {'uf': 'São Paulo', 'sigla': 'SP'}]".
print(brasil[0]) #Resultado: "{'uf': 'Rio de Janeiro', 'sigla': 'RJ'}".
print(brasil[1]) #Resultado: "{'uf': 'São Paulo', 'sigla': 'SP'}".
print(brasil[0]['uf']) #Resultado: "Rio de Janeiro".
print(brasil[1]['sigla']) #Resultado: "SP".

estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do estado: '))
    #brasil.append(estado[:]) | Importante: lembre-se de quebrar a conexão entre as listas. Porém, esse método de fatiamento não funciona com Dicionários.
    brasil.append(estado.copy()) #Somente dessa maneira se pode quebrar a conexão entre listas ao se usar Dicionários.
print(brasil)
#Resultado: o programa perguntará pela "Unidade Federativa" e "sigla do estado" e, após as respostas, mostrará os resultados na tela.
#P. S.: O resultado visual vai seguir este modelo: "{'uf': 'Rio de Janeiro', 'sigla': 'RJ'}".

estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do estado: '))
    brasil.append(estado.copy())
print(brasil)
for e in brasil:
    print(e)
#De novo, o resultado visual será parecido com esse "{'uf': 'Rio de Janeiro', 'sigla': 'RJ'}", porém distribuido entre linhas.

estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do estado: '))
    brasil.append(estado.copy())
print(brasil)
for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}.')

estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do estado: '))
    brasil.append(estado.copy())
print(brasil)
for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()
