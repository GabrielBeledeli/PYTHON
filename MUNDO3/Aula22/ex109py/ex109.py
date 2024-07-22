# Exercício Python 109: Modifique as funções que form criadas no desafio 107 para que elas aceitem um parâmetro a mais, informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.
import moedas
valor = float(input('Digite o preço: R$'))
print(f'Aumentando 10%, temos R${moedas.aumentar(valor, 10, True)}')
print(f'Descontando 10%, temos R${moedas.diminuir(valor, 10, True)}')
print(f'O dobro de {moedas.moeda(valor)} é {moedas.dobro(valor, True)}')
print(f'A metade de {moedas.moeda(valor)} é {moedas.metade(valor, True)}')