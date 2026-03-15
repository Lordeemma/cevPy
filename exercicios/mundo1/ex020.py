# Penúltimo exercício sobre módulos

from random import shuffle

a1 = str(input('Insira o nome do primeiro aluno: '))
a2 = str(input('Insira o nome do segundo aluno: '))
a3 = str(input('Insira o nome do terceiro aluno: '))
a4 = str(input('Insira o nome do quarto aluno: '))
list = [a1, a2, a3, a4]
shuffle(list)

print('A ordem de alunos sorteada foi: ')
print(list)