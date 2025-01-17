# Exercício Python 102: Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.

def fatorial(valor, show=True):
    """
    -> Calcula o fatorial de um número.
    :param n: O número a se calculado.
    :param show: (opicional) mostar ou não a conta.
    :return: O valor do Fatorial de um número n.    
    """
    f = 1
    for c in range(valor, 0 ,-1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f

# principal
help(fatorial)
num = int(input('Digite um número para receber o fatorial: '))
print(fatorial(num, True))
