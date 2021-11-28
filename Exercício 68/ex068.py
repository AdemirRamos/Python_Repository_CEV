print('Jogo do Par ou Ímpar')
print('')
print('-=' * 20)
print('Vamos jogar par ou ímpar!')
print('-=' * 20)
from random import randint
vitória = 0
while True:
    print('')
    jogador_valor = int(input('Escolha algum valor (entre 0 e 10): '))
    computador_número = randint(0, 10)
    soma_resultado = jogador_valor + computador_número
    tipo = ' '
    while tipo not in 'pi':
        tipo = str(input('Você escolhe "par" ou "ímpar"? ')).strip().lower()[0]
    print(f'Você jogou {jogador_valor} e o computador jogou {computador_número}.')
    print(f'A soma entre {jogador_valor} + {computador_número} é igual a: {soma_resultado}.')
    #print('deu par' if soma_resultado % 2 == 0 else 'deu ímpar') -> linha simplificada.

    if tipo == 'p':
        if soma_resultado % 2 == 0:
            print('O jogador venceu!')
            vitória += 1
        else:
            print('O computador venceu!')
            break
    elif tipo == 'i':
        if soma_resultado % 2 == 1:
            print('O jogador venceu!')
            vitória += 1
        else:
            print('O computador venceu!')
            break
    print('')
    print('Vamos jogar novamente!')
print('')
print('Fim de jogo. Você venceu {} vezes.'.format(vitória))
