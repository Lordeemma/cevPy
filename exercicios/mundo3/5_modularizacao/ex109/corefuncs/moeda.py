def metade(n, formatacao):
    n /= 2

    if formatacao:
        return formatar(n)
    else:
        return n

def dobro(n, formatacao):
    n *= 2

    if formatacao:
        return formatar(n)
    else:
        return n

def aumentar(n, aumento, formatacao):
    n += ((n*aumento)/100)

    if formatacao:
        return formatar(n)
    else:
        return n

def diminuir(n, reducao, formatacao):
    n -= ((n*reducao)/100)

    if formatacao:
        return formatar(n)
    else:
        return n

def formatar(n):
    valor = f'{n:.2f}'
    valorf = f'R${valor[0:len(valor)-3]},' + f'{valor[-2:]}'
    return valorf