# Mais outro exercício sobre o laço while

n1 = int(input('Insira o primeiro termo da PA: '))
r = int(input('Insira a razão da PA: '))
limit = int(input('Quantos termos você deseja visualizar? '))
seq = 0
c = 2

print(n1, end=' ')
while c <= limit: 
        seq += n1 + (c - 1) * r
        print(seq, end=' ')
        seq = 0
        c += 1