# Penúltimo exercício sobre módulos

from random import shuffle

student1 = str(input('Insira o nome do primeiro aluno: '))
student2 = str(input('Insira o nome do segundo aluno: '))
student3 = str(input('Insira o nome do terceiro aluno: '))
student4 = str(input('Insira o nome do quarto aluno: '))
list = [student1, student2, student3, student4]
shuffle(list)

print('A ordem de alunos sorteada foi: ')
print(list)