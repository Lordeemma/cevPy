# Mais outro exercício de condições

distance = float(input('Por quantos quilômetros você percorreu? '))
kmprice = 0

if distance < 200:
    kmprice = 0.5
else:
    kmprice = 0.45

fprice = distance * kmprice
print('Preço final: R${}'.format(fprice))

