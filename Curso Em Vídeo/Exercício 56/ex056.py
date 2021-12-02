print('Analisador Completo')
print()
somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totalmulher20 = 0
for p in range(1, 5):
    print('---' * 5, '{}ª Pessoa'.format(p), '---' * 5)
    nome = input('Nomde: ').strip()
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ').strip().upper()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff'and idade < 20:
        totalmulher20 += 1
mediaidade = somaidade / 4
print('A média de idade do grupo é de: {}'.format(mediaidade))
print('O homem mais velhor tem {} anos e se chama {}.'.format(maioridadehomem, nomevelho))
print('Ao todo são {} mulheres no grupo com menos de 20 anos de idade.'.format(totalmulher20))
