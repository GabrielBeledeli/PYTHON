"""
Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico. 
No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa 
vai informar quantas cédulas de cada valor serão entregues. OBS:
considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
"""
print('-'*40)
print(f'{' BANCO 123 ':^40}')
print('-'*40)
while True:
    valor = int(input('Qual valor você deseja sacar? R$'))
    total = valor
    cedulas_50 = 0
    cedulas_20 = 0
    cedulas_10 = 0
    cedulas_01 = 0
    cond = ' '
    
    if total >= 50:
       cedulas_50 = total//50
       total -= (50*cedulas_50)
       print(f'Total de {cedulas_50} cédulas de R$50.00')
    if total >= 20:
        cedulas_20 = total//20
        total -= (20*cedulas_20)
        print(f'Total de {cedulas_20} céculas de R$20.00')
    if total >= 10:
        cedulas_10 = total//10
        total -= (10*cedulas_10)
        print(f'Total de {cedulas_10} cédulas de R$10.00')
    if total >= 1:
        cedulas_01 = total//1
        total = (1*cedulas_01)
        print(f'Total de {cedulas_01} cédulas de R$1.00')

    while cond not in 'NS':
        cond = str(input('Deseja sacar novamente? [S/N] ')).strip().upper()[0]
    if cond == 'N':
        break
print('Tenha um bom Dia!\nVolte sempre!')
