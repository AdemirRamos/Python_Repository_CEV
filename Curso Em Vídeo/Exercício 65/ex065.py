print('Maior e Menor Valores')
print('')
resp = 'S'
soma = quantidade = média = maior = menor = 0
while resp in 'Ss':
    num = int(input('Digite um número: '))
    soma += num
    quantidade += 1
    if quantidade == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        elif num < menor:
            menor = num
    resp = str(input('Você quer continuar? [S/N]: ')).strip().upper()[0]
média = soma / quantidade
print('Você digitou {} números e a média foi: {}.'.format(quantidade, média))
print(f'O maior valor digitado foi {maior} e o menor valor foi {menor}.')
