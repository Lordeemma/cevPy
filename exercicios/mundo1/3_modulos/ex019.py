# Mais um exercício de módulos

from random import choice

student1 = str(input('Insira o nome do primeiro aluno: '))
student2 = str(input('Insira o nome do segundo aluno: '))
student3 = str(input('Insira o nome do terceiro aluno: '))
student4 = str(input('Insira o nome do quarto aluno: '))

print('O aluno sorteado para apagar o quadro foi o(a) {}'.format(choice([student1, student2, student3, student4])))
