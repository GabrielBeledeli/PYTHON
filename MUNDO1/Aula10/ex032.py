# Exercício Python 32: Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
ano = int(input('Que ano quer analizar? '))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é BISSEXTO!'.format(ano))
else:
    print('O ano {} nao é BISSEXTO!'.format(ano))