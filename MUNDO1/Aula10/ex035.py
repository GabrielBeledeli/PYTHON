# Exercício Python 35: Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
print('\033[32;43m=-=\033[m'*20)
print('{:.^60}'.format('Analizador de Triangulos'))
print('=-='*20)
r1 = float(input('Primeiro Segmento: '))
r2 = float(input('Segundo Segmento '))
r3 = float(input('Terceiro Segmento '))
if r1 < r2+r3 and r2 <r1+r3 and r3<r1+r2:
    print('Os segmentos acima podem formar triangulos')
else:
    print('Os segmentos acima não podem formar triangulos')