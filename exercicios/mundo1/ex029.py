# Outro exercício sobre condições

speed = float(input('Insira a velocidade do carro: '))
fine = (speed - 80) * 7

if speed > 80:
    print('Carro multado. A multa foi de R${}.'.format(fine))
else:
    print('Carro dentro das normas.')