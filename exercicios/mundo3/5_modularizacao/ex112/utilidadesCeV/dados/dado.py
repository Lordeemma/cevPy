def leiaDinheiro(msg):
    valor = 0

    while True:
        n = str(input(msg))

        if n.isnumeric():
            valor = float(n)
            return valor
        else:
            print('\033[1;31mInsira um valor válido.\033[m')
