# Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
jogador = dict()
partidas = list()
jogador['Nome'] = str(input('Nome do jogador: ')).strip()
jogos = int(input(f'Quantas partidas {jogador['Nome']} jogou? '))
print('=='*15)
for c in range(0, jogos):
    partidas.append(int(input(f'Quantos gols na {c+1}ª partida? ')))
jogador['Gols'] = partidas[:]
jogador['Total'] = sum(partidas)
print('=='*15)
print(jogador)
print('=='*15)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('=='*15)
print(f'O Jogador {jogador["Nome"]} jogou {len(jogador["Gols"])} partidas!')
print('=='*15)
for i, v in enumerate(jogador["Gols"]):
    print(f'Na partida {i+1}, fez {v} gols')
print(f'Foi um total de {jogador["Total"]} gols!!')