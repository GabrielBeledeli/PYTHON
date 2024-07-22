"""
Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:

[ 1 ] somar

[ 2 ] multiplicar

[ 3 ] maior

[ 4 ] novos números

[ 5 ] sair do programa

Seu programa deverá realizar a operação solicitada em cada caso."""
n1 = float(input('Primeiro Valor: '))
n2 = float(input('Segundo Valor: '))
condicao = False
while not condicao:
    print('[ 1 ] Somar\n[ 2 ] Multiplicar\n[ 3 ] Maior\n[ 4 ] Novos Números\n[ 5 ] Sair do programa')
    opcao = int(input('>>>>>>>>>>> Qual a sua opção? '))
    if opcao == 1:
        soma = n1+n2
        print('A soma entre {} + {} é {}'.format(n1,n2,soma))
        print('='*30)

    elif opcao == 2:
        multiplicacao = n1*n2
        print('A Multiplicação entre {} x {} é {}'.format(n1,n2,multiplicacao))
        print('='*30)

    elif opcao == 3:
        if n1 > n2:
            print('O mairo número entre {} e {} é {}'.format(n1,n2,n1))
            print('='*30)
        else:
            print('O mairo número entre {} e {} é {}'.format(n1,n2,n2))
            print('='*30)

    elif opcao == 4:
        n1 = float(input('Primeiro Valor: '))
        n2 = float(input('Segundo Valor: '))
        print('='*30)

    elif opcao == 5:
        condicao = True

    else:
        print('Opção invalida! Tente novamente.')
        print('='*30)
        