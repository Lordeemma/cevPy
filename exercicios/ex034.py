# Penúltimo exercício sobre condições

wage = float(input('Salário do funcionário: '))

if wage < 1250:
    print('O salário sofreu um aumento de 15%, agora sendo avaliado em R${}'.format((wage * 0.15) + wage))
else:
    print('O salário sofreu um aumento de 10%, agora sendo avaliado em R${}'.format((wage * 0.10) + wage))