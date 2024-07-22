# Exercício Python 65: Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
condicao = 's'
count = soma = maior = menor = 0

while 'n' not in condicao:
    n = float(input('Digite um número: '))
    condicao = str(input('Quer continuar? [s/n]'))
    count += 1
    soma += n
    if count == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        elif n < menor:
            menor = n
print('Você digitou {} valores e a média entre eles foi de {}'.format(count, soma/count))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))