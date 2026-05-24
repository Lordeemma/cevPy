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

def resumo(n, aumento, reducao):
    print('\033[1m-' * 30)
    print(f'{"RESUMO DO VALOR":^30}')
    print('-' * 30, end='')
    print('\033[m')

    print(f'{"Preço analisado:":<20}{formatar(n):>9}')
    print(f'{"Dobro do preço:":<20}{dobro(n, True):>9}')
    print(f'{"Metade do preço:":<20}{metade(n, True):>9}')
    print(f'{f"{aumento}% de aumento:":<20}{aumentar(n, aumento, True):>9}')
    print(f'{f"{reducao}% de redução:":<20}{diminuir(n, reducao, True):>9}')

    print('\033[1m-' * 30)