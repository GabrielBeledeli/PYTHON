# Exercício Python 114: Crie um código em Python que teste se o um site está acessível pelo computador usado.
import urllib
import urllib.request
user_agent = {'User-Agent': 'Chrome/58.0.3029.110'}
url = 'https://www.cursoemvideo.com'

try:
    req = urllib.request.Request(url, headers=user_agent)
    site = urllib.request.urlopen(req)
except urllib.error.URLError:
    print('Erro, conexão interrompida')
else:
    print('Conexão bem sucedida!')