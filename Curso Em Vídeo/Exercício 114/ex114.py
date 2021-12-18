print('O Site Está Acessível?')
print()

import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')

except urllib.error.URLError:
    print('O site "Pudim" não está acessível no momento.')

else:
    print('Site "Pudim" acessado com sucesso.')
    print(site.read()) #Esse comando "printa" o html do site acessado.
