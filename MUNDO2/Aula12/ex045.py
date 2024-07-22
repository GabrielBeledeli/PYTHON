# Exercício Python 45: Crie um programa que faça o computador jogar Jokenpô com você.
from random import randint
usuario = int(input('\033[36mSuas Opções:\n[ 0 ] PEDRA\n[ 1 ] PAPEL\n[ 2 ] TESOURA\nQual é a sua jogada? \033[m'))
computador = randint(0,2)
print('\033[32mJogada do computador: \033[m{}'.format(computador))
if computador == 0: #computador jogou PEDRA
    if usuario == 0:
        print('\033[34mEMPATE!!\033[m')
    elif usuario == 1:
        print('\033[34mVOCÊ GANHOU!!\033[m')
    elif usuario == 2:
        print('\033[34mVOCÊ PERDEU!!\033[m')
    else: print('TENTE NOVAMENTE!!')
elif computador == 1: #computador jogou PAPEL
    if usuario == 0:
        print('\033[34mVOCÊ PERDEU!!\033[m')
    elif usuario == 1:
        print('\033[34mEMPATE!!\033[m')
    elif usuario == 2:
        print('\033[34mVOCÊ GANHOU!!\033[m')
    else: print('TENTE NOVAMENTE!!')
elif computador == 2: #computador jogou TESOURA 
    if usuario == 0:
        print('\033[34mVOCÊ GANHOU!!\033[m')
    elif usuario == 1:
        print('\033[34mVOCÊ PERDEU!!\033[m')
    elif usuario == 2:
        print('\033[34mEMPATE!!\033[m')
    else: print('TENTE NOVAMENTE!!')
print('\033[32mTENTE NOVAMENTE\033[m')