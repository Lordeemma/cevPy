# Outro exercício sobre condições aninhadas 

n1 = float(input('Primeira nota do aluno: '))
n2 = float(input('Segunda nota do aluno: '))
avg = (n1 + n2) / 2

print('MÉDIA: {:.2f}'.format(avg))
if avg >= 7:
    print('SITUAÇÃO: APROVADO')
elif avg >= 5 and avg <= 6.9:
    print('SITUAÇÃO: RECUPERAÇÃO')
else:
    print('SITUAÇÃO: REPROVADO')