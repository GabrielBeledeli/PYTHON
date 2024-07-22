# Exercício Python 68: Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
from random import randint
count = 0
print('='*40)
print(f'{'VAMOS JOGAR PAR OU IMPAR: ':^40}')
print('='*40)
while True:
    n = int(input('Digite um valor de (0-10): '))
    opcao = str(input('Par ou ímpar [P/I]: ')).strip().upper()
    ia = 1
    print('='*40)
    print(f'Você jogou {n} e a IA {ia} | ', end='')
    soma = n+ia

    if soma % 2 == 0:
        print(f'Total {soma} PAR!')
        if 'P' in opcao:
            print('='*40)
            print('Você Venceu!')
            count += 1

        elif 'I' in opcao:
            print('='*40)
            print('Você Perdeu!')
            break
    else:
        print(f'Total {soma} ÍMPAR!')
        if 'I' in opcao:
            print('='*40)
            print('Você Venceu!')
            count += 1

        elif 'P' in opcao:
            print('='*40)
            print('Você Perdeu!')
            break

print(f'GAME OVER! Você venceu {count} vezes.')
