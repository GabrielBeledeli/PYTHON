# Exercício Python 095: Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
jogador = dict()
time = list()
partidas = list()
while True:
    jogador.clear()
    partidas.clear()
    jogador['Nome'] = str(input('Nome do jogador: ')).strip()
    jogos = int(input(f'Quantas partidas {jogador['Nome']} jogou? '))
    print('=='*15)
    for c in range(0, jogos):
        partidas.append(int(input(f'Quantos gols na {c+1}ª partida? ')))
    jogador['Gols'] = partidas[:]
    jogador['Total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
        if resp in 'SN':
            break           
    if resp == 'N':
        break
print('=='*20)
print('Cod  ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('=='*20)
for k, v in enumerate(time):
    print(f'{k:<4} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('=='*20)
while True:
    busca = int(input('Buscar dados de qual jogador? (999 STOP) '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'Erro não existe jogador com código {busca}!')
    else:
        print('=='*20)
        print(f'Levantameto do Jogador: {time[busca]["Nome"]}')
        print('=='*20)
        for i, g in enumerate(time[busca]["Gols"]):
            print(f'  No jogo {i+1} fez {g} gols!')
    print('=='*20)
print('<<< ENCERRADO >>>')