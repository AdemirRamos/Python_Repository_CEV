print('Validando Entrada de Dados em Python')
print()

def leia_int(message):
    ok = False
    valor = 0
    while True:
        n = str(input(message))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mErro! Digite um valor válido (um número inteiro).\033[m')
        if ok: #Se "ok" == "True".
            break
    return valor

n = leia_int('Digite um número: ')
print(f'Você acabou de digitar o número {n}.')
