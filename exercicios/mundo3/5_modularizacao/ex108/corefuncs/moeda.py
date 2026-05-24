def metade(n):
    n /= 2
    return n

def dobro(n):
    n *= 2
    return n

def aumentar(n, aumento):
    n += ((n*aumento)/100)
    return n

def diminuir(n, reducao):
    n -= ((n*reducao)/100)
    return n

def formatar(n):
    valor = f'{n:.2f}'
    valorf = f'R${valor[0:len(valor)-3]},' + f'{valor[-2:]}'
    return valorf