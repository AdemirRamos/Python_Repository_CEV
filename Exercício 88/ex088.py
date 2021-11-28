print('Palpites Para a Mega-Sena')
print('-=' * 30)
print('{:^20} Jogo da Mega-Sena')
import random
jogo_mega = []
jogo = int(input('Quantos jogos você quer que eu sorteie? Digite um número: '))
print()
for c in range(0, 5):
    números = random.randint(0, 60)
    jogo_mega.insert(c, números)
for c in range(1, jogo + 1):
    print(f'O {c}ª jogo sorteado foi: {jogo_mega}')

#Fiz o exercício quase completamente (mas, no final, não consegui achar um jeito de completá-lo). Resolução do Guanabara:

print('Palpites Para a Mega-Sena')
print('-=' * 30)
print('{:^20} Jogo da Mega-Sena')