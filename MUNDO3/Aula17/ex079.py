# Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
valores = []
while True:
    n = int(input('Digite um valor: '))
    if n not in valores:
        valores.append(n)
        print('Valor Adicionado...')
    else:
        print('Valor Duplicado! Não vou adicionar!')
    r = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if r in 'N':
        break      
print('='*30)
print(f'Você digitou os valores: {sorted(valores)}')