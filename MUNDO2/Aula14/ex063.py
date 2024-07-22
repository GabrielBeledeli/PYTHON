# Exercício Python 63: Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. Exemplo:
print('{:=^36}'.format(' Sequencia de Fibonacci '))
n = int(input('Quantos termos você quer mostrar? '))
cont = 3
t1 = int(0)
t2 = int(1)
print('{} -> {} -> '.format(t1, t2), end='')
while cont != n:
    t3 = t1+t2
    t1 = t2
    t2 = t3
    print('{}'.format(t3), end=' -> ')
    cont += 1
print('FIM', end='')