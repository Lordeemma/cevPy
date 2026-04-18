# Mais um exercício sobre o laço while

limit = int(input('Quantos elementos da sequeência de Fibonacci deseja visualizar? '))
c = 2

n1 = 0
n2 = 1
a = 0
print(n1, end=' ')

while c < limit:
    print(n1, end=' ')
    a = n1 + n2
    n1 = n2
    n2 = a
    c += 1