# Exercício Python 61: Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.
print('{:=^36}'.format(' Gerrador de PA '))
p_t = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))
cont = 0
pa = p_t
while cont != 10:
    print('{}'.format(pa), end=' -> ')
    pa += r
    cont += 1
print('FIM')
