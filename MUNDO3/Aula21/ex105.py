# Exercício Python 105: Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
def notas(*notas, situação):
    valores = dict()
    media = 0
    for v in notas:
        media += v
    media /= len(notas) 
    valores['Total:'] = len(notas)
    valores['Maior:'] = max(notas)
    valores['Menor:'] = min(notas)
    valores['Média:'] = media
    if situação:
        if media >= 9.0:
            valores['Situaão:'] = 'EXELENTE'
        elif 7.0 <= media < 9.0:
            valores['Situaão:'] = 'BOA'
        elif 6.0 <= media < 7.0:
            valores['Situaão:'] = 'RUIM'
        else:
            valores['Situaão:'] = 'PÉSSIMA'
    return valores
# principal
resp = notas(8,0,0,9, situação=False)
print(resp)