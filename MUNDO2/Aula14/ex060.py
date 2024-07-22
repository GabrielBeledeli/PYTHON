 # Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial.
'''from math import factorial
n = int(input('Digite um número para receber seu fatorial: '))
f = factorial(n)
print('O fatorial de {} é {}'.format(n,f))'''

n = int(input('Informe um número para receber seu fatorial: '))
c = n
f = 1
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))
