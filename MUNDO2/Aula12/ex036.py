# Exercício Python 36: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
print('\033[32m-'*20)
print('Simulação de Emprestimos')
print('-'*20)
print('\033[m')
valor = float(input('Valor da casa: R$'))
parcelas = int(input('Quantidade de anos: '))
renda = float(input('Sua renda mensal: R$'))

preco_p = valor / (parcelas*12)
verificacao = preco_p / renda

print('Valor da parcela: R${}'.format(preco_p))

if verificacao <= 0.30:
    print('Aprovado')
else:
    print('Reprovado')
    