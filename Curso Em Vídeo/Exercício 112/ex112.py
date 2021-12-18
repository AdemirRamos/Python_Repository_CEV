print('Entrada de Dados Monetários')
print()

import resumo

def leia_dinheiro(message):
    válido = False
    while not válido:
        entrada = str(input(message)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'\033[0;31mErro: \"{entrada}\" é um preço inválido.\033[m')
        else:
            válido = True
            return float(entrada)

preço = leia_dinheiro('Digite o preço: R$')
resumo.math(preço, 35, 22)
#