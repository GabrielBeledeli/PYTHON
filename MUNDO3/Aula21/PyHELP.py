from time import sleep
from deep_translator import GoogleTranslator
import io
import sys

# Cores para formatação
cores = ['\033[m',           # 0 sem cor
         '\033[0;30;41m',    # 1 vermelho
         '\033[0;30;42m',    # 2 verde   
         '\033[0;30;43m',    # 3 amarelo
         '\033[0;30;44m',    # 4 azul
         '\033[0;30;45m',    # 5 roxo
         '\033[40m']         # 6 branco

def dividir_texto(texto, max_caracteres=5000):
    partes = []
    parte_atual = ""
    
    for linha in texto.splitlines(True):  # Mantém os caracteres de nova linha
        if len(parte_atual) + len(linha) > max_caracteres:
            partes.append(parte_atual)
            parte_atual = linha
        else:
            parte_atual += linha
    
    if parte_atual:
        partes.append(parte_atual)
    
    return partes

def traduzir_texto(texto, max_caracteres=5000):
    tradutor = GoogleTranslator(source='auto', target='pt')
    partes = dividir_texto(texto, max_caracteres)
    texto_traduzido = ""
    for parte in partes:
        try:
            texto_traduzido += tradutor.translate(parte)
        except Exception as e:
            print(f"Erro ao traduzir parte do texto: {e}")
            texto_traduzido += parte  # Adiciona o texto original em caso de erro
    return texto_traduzido

def ajuda(com):
    titulo(f'Acessando o manual do comando \'{com}\'', 4)

    # Captura a saída da função help() em um buffer
    buffer = io.StringIO()
    sys.stdout = buffer
    help(com)
    sys.stdout = sys.__stdout__
    
    # Obtém o texto do buffer
    ajuda_texto = buffer.getvalue()
    
    # Traduz o texto para o português
    traduzido = traduzir_texto(ajuda_texto)
    
    print(cores[6])
    print(traduzido)
    print(cores[0])

def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(cores[cor])
    print('~' * tam)
    print(f'  {msg}  ')
    print('~' * tam)
    print(cores[0])

# Principal
while True:
    titulo('SISTEMA DE AJUDA PyHELP', 2)
    comando = str(input('Função ou Biblioteca > '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('ATÉ LOGO', 1)
