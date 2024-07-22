# Exercício Python 106: Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará. Importante: use cores.
cores = ['\033[m',           # 0 sem cor
     '\033[0;30;41m',    # 1 vermelho
     '\033[0;30;42m',    # 2 verde   
     '\033[0;30;43m',    # 3 amarelo
     '\033[0;30;44m',    # 4 azul
     '\033[0;30;45m',    # 5 roxo
     '\033[40m']       # 6 branco
def ajuda(com):
    titulo(f'Acessando o manual do comando \' {com} \'',4)

    print(cores[6])
    help(com)
    print(cores[0])

def titulo(msg, cor=0):
    tam = len(msg)+4
    print(cores[cor])
    print('~'*tam)
    print(f'  {msg}  ')
    print('~'*tam)
    print(cores[0])


# principal
while True:
    titulo('SISTEMA DE AJUDA PyHELP', 2)
    comando = str(input('Função ou Biblioteca > '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('ATÉ LOGO', 1)
