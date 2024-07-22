# Exercício Python 113: Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.
def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except(ValueError, TypeError):
            print('\033[31mERRO, por favor digite um número inteiro válido\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[31mERRO, entrada de dados interrompida pelo usuário\033[m')
            return 0
        else:
            return n
def leiafloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO, por favor digite um número real válido\033[m')
        except (KeyboardInterrupt):
            print('\033[31mERRO, entrada de dados interrompida pelo usuário\033[m')
            return 0
        else:
            return n
# principal
n1 = leiaint('Digite um inteiro: ')
n2 = leiafloat('Digite um real: ')
print(f'O valor inteiro digitado foi {n1} e o real foi {n2}')