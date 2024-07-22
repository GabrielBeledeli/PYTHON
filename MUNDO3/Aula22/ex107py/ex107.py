# Exercício Python 107: Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.
import moeda
valor = float(input('Digite o preço: R$'))
precos = (moeda.aumentar(valor), moeda.diminuir(valor), moeda.dobro(valor), moeda.metade(valor))
print(f'Aumentando 10%, temos R${precos[0]}')
print(f'Descontando 10%, temos R${precos[1]}')
print(f'O dobro de {valor} é {precos[2]}')
print(f'A metade de {valor} é {precos[3]}')