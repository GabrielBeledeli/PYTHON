# Exercício Python 55: Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
maior_p = 0
menor_p = 0
for c in range(0,5):
    peso = float(input('Peso da {}º pessoa: '.format(c+1)))
    if c == 0:
        maior_p = peso
        menor_p = peso
    else:
        if peso < menor_p:
            menor_p = peso
        elif peso > maior_p:
            maior_p = peso
    
print('O maior peso é {}Kg\nO menor peso é {}Kg'.format(maior_p,menor_p))
