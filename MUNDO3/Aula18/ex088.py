# Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
from random import randint
print('='*60)
print(f'{'MEGA SENA':^60}')
print('='*0)
qunat_jogos = int(input('Quantos jogos serão gerados? '))
lista = list()
print('-='*10, f'SORTEANDO {qunat_jogos} JOGOS', '-='*10)
for c in range(0, qunat_jogos):
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    print(f'Os números sorteados foram: {lista}')
    lista.clear()