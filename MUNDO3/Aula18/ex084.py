# Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:A) Quantas pessoas foram cadastradas.B) Uma listagem com as pessoas mais pesadas.C) Uma listagem com as pessoas mais leves.
dados_temp = list()
lista = list()
maior = menor = float(0)
while True:
    print('=-='*10)
    dados_temp.append(str(input('Nome: ')).strip())
    dados_temp.append(float(input('Peso: ')))

    if len(lista) == 0:
        maior = menor = dados_temp[1]
    else:
        if dados_temp[1] > maior:
            maior = dados_temp[1]
        if dados_temp[1] < menor:
            menor = dados_temp[1]

    lista.append(dados_temp[:])
    dados_temp.clear()
    cond = ' '
    while cond not in 'NS':
        cond = str(input('Quer Continuar? [S/N] ')).strip().upper()[0]
    if cond == 'N':
        break
# print(f'Os dados foram {lista}')
print(f'A quantidade de pessoas cadastradas é {len(lista)}')
print(f'Os maiores pessos foram de ', end='')
for p in lista:
    if p[1] == maior:
        print(f'{p[0]}', end=' ')
print(f'\nOs menores pesos foram de ', end='')
for p in lista:
    if p[1] == menor:
        print(f'{p[0]}', end=' ')
        