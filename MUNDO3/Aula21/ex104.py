# Exercício Python 104: Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante ‘a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico. Ex: n = leiaInt(‘Digite um n: ‘)
def leiaint(txt):
    valor = 0
    cond = False
    while True:
        conf = str(input(txt)).strip()
        if conf.isnumeric():
            valor = conf
            cond = True
        else:
            print('ERRO! Digite um número inteiro válido!')
        if cond:
            break
    return valor
# principal 
n = leiaint('Digite um número: ')
print(f'Você digitou o número {n}')