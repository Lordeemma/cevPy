# Mais outro exercício sobre o laço for

n1 = int(input('Insira o primeiro termo da PA: '))
r = int(input('Insira a razão da PA: '))
seq = 0

print(n1)
for i in range(2, 10 + 1): 
        seq += n1 + (i - 1) * r
        print(seq)
        seq = 0


