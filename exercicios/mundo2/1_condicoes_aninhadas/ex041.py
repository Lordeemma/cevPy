# Mais outro exercício sobre condições aninhadas

from datetime import date

print('CATEGORIZAÇÃO DE ATLETAS DE NATAÇÃO')
born_year = int(input('Qual é seu ano de nascimento? '))
age = date.today().year - born_year

if age > 25:
    print('CATEGORIA: MASTER')
elif age >= 19 and age <= 25:
    print('CATEGORIA: SÊNIOR')
elif age >= 14 and age < 19:
    print('CATEGORIA: JÚNIOR')
elif age >= 9 and age < 14:
    print('CATEGORIA: INFANTIL')
else:
    print('CATEGORIA: MIRIM')
