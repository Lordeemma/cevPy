# Exercício sobre interrupções do laço while

n = 0
c = 0

while True:
    s = int(input('Digite um valor (999 para interromper): '))

    if s == 999:
        break

    n += s
    c += 1

print(f'A soma dos {c} valores foi {n}')