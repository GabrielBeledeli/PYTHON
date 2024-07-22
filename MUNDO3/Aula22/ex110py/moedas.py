def aumentar(v=0, taxa=0, formato=False):
    res = v + (v*taxa/100)
    return res if formato is False else moeda(res)
def diminuir(v=0, taxa=0, formato=False):
    res = v - (v*taxa/100)
    return res if formato is False else moeda(res)
def dobro(v=0, formato=False):
    res = v*2
    return res if not formato else moeda(res)
def metade(v=0, formato=False):
    res = v/2
    return res if not formato else moeda(res)
def moeda(v=0, moeda='R$'):
    return f'{moeda}{v:.2f}'.replace('.', ',')
def resumo(v=0, taxaa=10, taxar=5):
    print('-'*32)
    print('RESUMO DO VALOR'.center(32))
    print('-'*32)
    print(f'Preço analisado: \t{moeda(v)}')
    print('-'*32)
    print(f'Dobro do preço: \t{dobro(v, True)}')
    print(f'Metade do preço: \t{metade(v, True)}')
    print(f'Com {taxaa}% de aumento: \t{aumentar(v, taxaa, True)}')
    print(f'COm {taxar}% de desconto: \t{diminuir(v, taxar, True)}')
    print('-'*32)