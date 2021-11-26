print('Dicionário em Python')
print()
nome = input('Nome: ')
média_pessoa = float(input(f'Média de {nome}: '))
pessoa = {'nome': nome, 'média': média_pessoa}
print()
print(f'Nome é igual a "{pessoa["nome"]}".')
print(f'Média é igual a "{pessoa["média"]}".')
if média_pessoa >= 6.0:
    print(f'A situação do aluno (a) {pessoa["nome"]} é: "aprovado (a)".')
else:
    print(f'A situação do aluno (a) {pessoa["nome"]} é: "reprovado (a)".')

#Resolução do Guanabara:

aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['média'] = float(input(f'Média de: {aluno["nome"]}')) #se deve usar aspas duplas aqui (com o dicionário) para se evitar erros.
if aluno['média'] >= 7:
    aluno['situação'] = 'Aprovado (a).'
elif 5 <= aluno['média'] < 7:
    aluno['situação'] = 'Recuperação.'
else:
    aluno['situação'] = 'Reprovado (a).'
print('-=' * 30)
for k, v in aluno.items():
    print(f' - {k} é igual a {v}.')
