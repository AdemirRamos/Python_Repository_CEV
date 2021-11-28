print('Soma De Ímpares e Múltiplos de Três')
print()
soma = 0 #Responsável pela soma.
count = 0 #Responsável pela contagem dos números ímpares.
for ímpares in range(1, 501, 2):
    if ímpares % 3 == 0:
        soma = soma + ímpares
        count = count + 1 #Essa conta só os divisíveis por 3.
    #count = count + 1 -> Essa linha de código contaria todos os números ímpares da sequência.
        #print(ímpares, end=' ') -> Essa linha de código alinha todos os números com um espaço entre eles
print('A soma de todos esses números ({} no total) é igual a: {}.'.format(count, soma))
#variável += v -> == variável + variável = v.
