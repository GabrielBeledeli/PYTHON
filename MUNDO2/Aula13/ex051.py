# Exercício Python 51: Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.
p = int(input('Primeiro termo: '))
r = int(input('Digite a razão: '))
d = p + (10-1)*r
for i in range(p, d + r, r):
    print('{}'.format(i), end=' -> ')
print('ACABOU')