# Último exercício sobre o laço for

name_m_older = 0
age_m = 0
less_20_w = 0
avg = 0

for i in range (1, 4 + 1):
    name = str(input('Nome: '))
    age = int(input('Idade: '))
    sex = str(input('Sexo [H/M]: '))
    sex = sex.strip().lower()

    if sex == 'h' and age > age_m:
        age_m = age
        name_m_older = name

    if sex == 'm' and age < 20:
        less_20_w += 1

    avg += age

avg = avg / 4

print('Média de idade: {}'.format(avg))
print('Nome do homem mais velho: {}'.format(name_m_older))
print('Mulheres com menos de 20 anos: {}'.format(less_20_w))