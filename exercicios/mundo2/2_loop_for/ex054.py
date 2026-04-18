# Outro exercício sobre o laço for

from datetime import date

great = 0
less = 0

for i in range (1, 7 + 1):
    year = int(input('Insira o ano de nascimento da {}ª pessoa: '.format(i)))
    age = date.today().year - year

    if age < 18:
        less += 1
    elif age >= 18:
        great += 1

print('Maiores de 18: {}'.format(great))
print('Menores de 18: {}'.format(less))