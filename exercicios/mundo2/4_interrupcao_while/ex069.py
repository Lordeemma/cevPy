# Mais outro exercício sobre interrupção do laço while

over_18 = 0
men = 0
women_below_20 = 0

while True:
    age = int(input('Qual é sua idade? '))
    gender = str(input('Qual é seu gênero [H/M]? ')).strip()

    if age > 18:
        over_18 += 1

    if gender.lower() == 'h':
        men += 1

    if age < 20 and gender.lower() == 'm':
        women_below_20 += 1

    choice = str(input('Deseja continuar [S/N]? '))

    if choice.lower() == 'n':
        break
    else:
        continue

print(f'Pessoas com mais de 18 anos: {over_18}')
print(f'Quantidade de homens: {men}')
print(f'Mulheres com menos de 20 anos: {women_below_20} ')