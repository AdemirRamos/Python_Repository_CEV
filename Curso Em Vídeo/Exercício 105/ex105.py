print('Analisando e Gerando Dicionários')
print()

def notas(* n, situação = True):
    """

    A função "notas" permite que o usuário digite vários números, após isso, será apresentado um dicionário com informações sobre os números digitados.

    - parâmetro n: nesse parâmetro serão inseridos todos os números digitados pelo usuário;
    - parâmetro situação: caso seja "True", esse parâmetro mostrará uma mensagem indicando a "situação do usuário"; caso seja "False", não mostrará nada;
    - return: retorna para o dicionário "r" todos os dados analisados pela função notas.
    
    """
    print()
    r = dict()
    r['Total'] = len(n)
    r['Maior'] = max(n)
    r['Menor'] = min(n)
    r['Média'] = sum(n) / len(n)

    if situação: #Se a "situação" for == "True".
        if r['Média'] >= 7:
            r['Situação'] = 'Boa!'
        elif r['Média'] >= 5:
            r['Situação'] = 'Razoável.'
        else:
            r['Situação'] = 'Ruim!'
            
    return r

resposta = notas(9, 10, 5.5, 2.5, 9, 8.5)
print(resposta)
help(notas)
