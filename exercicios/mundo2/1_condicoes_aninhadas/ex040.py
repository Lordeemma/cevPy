# Outro exercício sobre condições aninhadas 

grade1 = float(input('Primeira nota do aluno: '))
grade2 = float(input('Segunda nota do aluno: '))
average = (grade1 + grade2) / 2

print('MÉDIA: {:.2f}'.format(average))
if average >= 7:
    print('SITUAÇÃO: APROVADO')
elif average >= 5 and average <= 6.9:
    print('SITUAÇÃO: RECUPERAÇÃO')
else:
    print('SITUAÇÃO: REPROVADO')