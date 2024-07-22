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