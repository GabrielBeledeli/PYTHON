# Exercício Python 099: Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
def maior(*num):
    count = maior = 0
    print('-'*40)
    print('Analizando os  valores passados...')
    for v in num:
      print(f'{v} ', end='')
    print(f'\nForam informados {len(num)} valores.')
    print(f'O maior valor é {max(num)}')

        
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(0)