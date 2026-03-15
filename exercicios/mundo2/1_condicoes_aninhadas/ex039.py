# Mais outro exercício sobre condições aninhadas

from datetime import date

born_year = int(input('Qual é seu ano de nascimento? '))
age = date.today().year - born_year

if age < 18:
    print('Você ainda não pode se alistar. Faltam {} anos.'.format(18 - age))
elif age == 18:
    print('Este é o ano de alistamento.')
else:
    print('O ano de alistamento já passou há {} anos'.format(age - 18))