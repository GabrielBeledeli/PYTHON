# Exercício Python 30: Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
num = int(input('Digite um numero para saber se ele é par ou impar: '))
if num % 2 == 0:
    print('PAR')
else:
    print('IMPAR')