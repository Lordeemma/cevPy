# Último exercício sobre operações aritméticas

daily_rent = int(input('Por quantos dias o carro foi alugado? '))
km = float(input('Por quantos quilômetros ele percorreu? '))
final_price = (daily_rent * 60) + (km * 0.15)

print('O preço final do aluguel foi de R${:.2f}'.format(final_price))

