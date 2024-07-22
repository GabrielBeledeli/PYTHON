# Exercício Python 091: Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
from random import randint
from time import sleep
from operator import itemgetter
jogadores = dict()
jogadores['Jogador 1'] = randint(1,6)
jogadores['jogador 2'] = randint(1,6)
jogadores['Jogador 3'] = randint(1,6)
jogadores['jogador 4'] = randint(1,6)
ranking = list()
print('Valores Sorteados: ')
for k, v in jogadores.items():
    sleep(0.5)
    print(f'{k} tirou [{v}] no dado')
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
print('=-='*9)
print(f'{'Ranking':^27}')
for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} com [{v[1]}]')