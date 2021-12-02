print('Contando Vogais Em Tupla')
print()
palavras = 'Aprender', 'Programar', 'Linguagem', 'Python', 'Curso', 'Gratis', 'Estudar', 'Praticar', 'Trabalhar', 'Mercado', 'Programador', 'Futuro'
for posição in palavras:
        print(f'\nNa palavra {posição} temos as seguintes vogais: ', end='')
        for letra in palavras:
              if letra.lower() in 'aáãàeéèiíoóuú':
                      print(letra, end=' ')
