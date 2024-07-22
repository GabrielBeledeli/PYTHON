# Exercício Python 097: Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.    
def escreva(f):
    s = len(f) + 4
    print('~'*s)
    print(f'  {f}')
    print('~'*s)

frase = str(input('Digite uma frase: ')).strip()
escreva(frase)