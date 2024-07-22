# Exercício Python 37: Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
num = int(input('Digite o valor a ser convertido: '))
c = int(input('''Selecione a opção:
[1] Binário
[2] Octal
[3] Hexadecimal
Sua Opção: '''))
if c == 1:
    print('O valor {} em Binário é: {}'.format(num, bin(num)[2:]))
elif c == 2:
    print('O valor {} em Octal é {}'.format(num, oct(num)[2:]))
elif c == 3:
    print('O valor {} em Hexadecimal é {}'.format(num, hex(num)[2:]))
else: print('Valor digitado não corresponde a nenhuma opção')