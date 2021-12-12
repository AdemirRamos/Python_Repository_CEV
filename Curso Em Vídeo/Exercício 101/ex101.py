print('Função Para Votações')
print()
def voto():
    nascimento = int(input('Digite o seu ano de nascimento: '))
    idade = 2021 - nascimento
    if idade < 16:
        print(f'Você tem {idade} anos de idade. Você tem menos de 16 anos. Para você, o voto não é obrigatório nem facultativo.')
    elif idade <= 17:
        print(f'Você tem {idade} anos de idade. A sua idade está entre 16 e 18 anos. Para você, o voto é facultativo.')
    elif idade < 65:
        print(f'Você tem {idade} anos de idade. A sua idade está entre 18 e 65 anos. Para você, o voto é obrigatório.')
    else:
        print(f'Você tem {idade} anos de idade. A sua idade é maior do que 65 anos. Para você, o voto é facultativo.')
voto()

#Resolução do Guanabara:

print('Função Para Votações')
print()

def voto(ano):

    #Escopo de importação: se configura quando uma importação é feita somente para um trecho específico do programa. 

    from datetime import date
    
    atual = date.today().year
    idade = atual - ano

    if idade <= 16:
        return f'Com {idade} anos, o voto não é permitido.'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos, o voto é opcional.'
    else:
        return f'Com {idade} anos, o voto é obrigatório.'

#Linhas opcionais:

#nascimento = int(input('Em que ano você nasceu? '))
print(voto(1990))
#print(voto(nascimento))
