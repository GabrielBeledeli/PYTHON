# Exercício Python 098: Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. Seu programa tem que realizar três contagens através da função criada:  
def contador(inicio, fim, passo):
    if inicio > fim:
        for c in range(inicio, fim-1, -passo):
            print(c, end=' -> ')
        print('FIM')
    else:
        for c in range(inicio, fim+1, passo):
            print(c, end=' -> ')
        print('FIM')
contador(1, 10, 1)
contador(10, 0, 2)
print('Contagem personalizada: ')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)
