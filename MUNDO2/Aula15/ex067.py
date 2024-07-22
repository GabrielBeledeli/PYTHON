# Exercício Python 67: Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.
while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    c = 1
    if n < 0:
       break
    else: 
        while c <= 10:
            print(f'{n} X {c:2} = {n*c}') 
            c += 1
print('Programa de tabuada encerrado!')