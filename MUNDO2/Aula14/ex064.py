# Exercício Python 64: Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
condicao = True
count = 0
soma = 0
while condicao:
    n = int(input('Digite um número [999 para parar]: '))
    if n == 999:
        condicao = False
    if n != 999:
        soma += n
        count += 1
print('Você digitou {} números e a soma entre eles foi de {}'.format(count,soma))
