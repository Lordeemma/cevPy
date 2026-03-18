# Penúltimo exercício sobre condições

wage = float(input('Salário do funcionário: '))
increase = 0

if wage < 1250:
    increase = 15
else:
    increase = 10

final_wage = wage + ((wage * increase) / 100)

print('O salário sofreu um aumento de {}%, agora sendo avaliado em R${}'.format(increase, final_wage))