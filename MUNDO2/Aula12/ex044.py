'''Exercício Python 44: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:

– à vista dinheiro/cheque: 10% de desconto

– à vista no cartão: 5% de desconto

– em até 2x no cartão: preço formal 

– 3x ou mais no cartão: 20% de juros'''

print('\033[1;33;40m{:=^80}\033[m'.format('LOJA DO ZÉ'))
preco = float(input('\033[32mPreco das compras: \033[mR$'))
print('\033[33m[ 1 ] à vista dinheiro/cheque\n[ 2 ] à vista cartão\n[ 3 ] 2x no cartão\n[ 4 ] 3x ou mais no cartão\033[m')
opcao = int(input('\033[1;31mQual a sua opção? \033[m'))
if opcao == 1:
    preco_f = preco - (preco*10/100)
    print('\033[32mSua compra de \033[mR${:.2f} \033[32mvai custar \033[mR${:.2f} \033[32mà vista no dinheiro/cheque.\033[m'.format(preco, preco_f))
elif opcao == 2:
    preco_f = preco - (preco*5/100)
    print('\033[32mSua compra de \033[mR${:.2f} \033[32mvai custar \033[mR${:.2f} \033[32mà vista no cartão.\033[m'.format(preco, preco_f))
elif opcao == 3:
    print('\033[32mSua compra parcelada em\033[m 2x \033[32mde \033[mR${:.2f} \033[32mSEM JUR0S custará \033[mR${:.2f}'.format(preco/2, preco))
elif opcao == 4:
    parcelas = int(input('\033[32mQunatas parcelas? \033[m'))
    preco_f = preco+(preco*20/100)
    preco_p = preco_f / parcelas
    print('\033[32mSua compra parcelada em \033[m{}x \033[32mde \033[mR${:.2f} \033[32mCOM JUROS custará \033[mR${:.2f}'.format(parcelas, preco_p, preco_f))
print('\033[1;33;40m{:=^80}\033[m'.format('COMPRA CONCLUÍDA'))