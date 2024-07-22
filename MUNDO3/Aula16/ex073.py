'''Exercício Python 73: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:

a) Os 5 primeiros times.

b) Os últimos 4 colocados.

c) Times em ordem alfabética.

d) Em que posição está o time do Palmeiras.'''

brasileirao_2024 = ('Flamengo', 'Botafogo', 'Palmeiras', 'Bahia', 'São Paulo', 'Cruzeiro', 'Athletico-PR', 'Fortaleza', 'Bragantino', 'Vasco da Gama', 'Internacional', 'Juventude', 'Atlético-MG', 'Criciúma', 'EC Vitória', 'Cuiabá', 'Corinthians', 'Grêmio', 'Atlético-GO', 'Fluminense')
print(brasileirao_2024)
print('-'*40)
print(f'Os cincos primeiros são {brasileirao_2024[:5]}')
print('-'*40)
print(f'Os quatro últimos são {brasileirao_2024[-4:]}')
print('-'*40)
print(f'Os times em ordem alfabética: {sorted(brasileirao_2024)}')
print('-'*40)
print(f'O Palmeiras está na {brasileirao_2024.index('Palmeiras')+1}ª posição')