# Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.
valores = list()
pares = list()
impares = list()
while True:
    num = (int(input('Digite um número: ')))
    valores.append(valores)
    if num % 2 == 0: 
        pares.append(num)
    else:
        impares.append(num)
    resp = str(input('Deseja Continuar? [S/N] ')).strip()[0]
    if resp in 'Nn':
        break
print(f'A lista completa é {num}')
print(f'A lista de pares é {pares}')
print(f'A lista de impares é {impares}')
