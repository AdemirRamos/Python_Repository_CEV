print('Validação De Dados')
print('')
sexo = input('Informe o seu sexo: ').strip().upper()[0]
while sexo not in 'FM':
    sexo = input('Dados inválidos. Por favor, informe o seu sexo: ').strip().upper()[0]
print('Sexo {} registrado.'.format(sexo))
