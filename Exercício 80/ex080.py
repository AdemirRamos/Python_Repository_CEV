print('Lista Ordenada Sem Repetições')
print()
lista = []
for c in range(0, 5):
    número = int(input('Digite um valor: '))
    if c == 0:
        lista.append(número)
    if número > len(lista) - 1:
    #Essa linha também poderia ser escrita assim: if número > lista [-1]:
        lista.append(número)
        print('Adicionado ao final da lista.')
    #Versão simplificada: if c == 0 or n > lista [-1]:
    else:
        posição = 0
        while posição < len(lista):
            if número <= lista[posição]:
                lista.insert(posição, número)
                print(f'Adicionado na posição {posição}ª da lista.')
                break
            posição += 1
print(f'Os valores digitados, em ordem, foram: {lista}')
