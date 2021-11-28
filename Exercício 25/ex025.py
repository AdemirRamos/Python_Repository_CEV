print('Procurando Uma String Dentro Da Outra')
print()
nome = str(input('Digite o seu nome completo: ')).strip()
print('O seu primeiro nome é "Silva"? {}.'.format(nome[:5] == 'Silva'))
print('')
nome = str(input('Digite o seu nome: ')).strip()

#print('No seu nome há "Silva"? {}'.format('Silva' in nome))
#print('No seu nome há "Silva?" {}'.format('SILVA' in nome.upper()))

print('No seu nome há "Silva"? {}'.format('silva' in nome.lower()))

#A primeira linha anulada acima só aceita "Silva" capitalizado; já a 2ª e 3ª linhas são maneiras de resolver esse problema.
