print('Progressão Aritimética')
print()
print('-=-' * 10)
print('10 Termos de uma PA')
print('-=-' * 10)
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
décimo = primeiro + (10 - 1) * razão
for p in range(primeiro, décimo + razão, razão):
    print('{}'.format(p), end=' -> ')
print('Acabou!')
