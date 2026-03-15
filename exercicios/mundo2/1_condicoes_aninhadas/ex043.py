# Outro exercício sobre condições aninhadas

print('CALCULADORA DE IMC')
weight = float(input('Insira seu peso em kg: '))
height = float(input('Insira sua altura em m: '))
bmi = weight / height**2

print('IMC: {:.2f}'.format(bmi))
if bmi > 40:
    print('CONDIÇÃO: OBESIDADE MÓRBIDA')
elif bmi >= 30 and bmi <= 40:
    print('CONDIÇÃO: OBESIDADE')
elif bmi >= 25 and bmi < 30:
    print('CONDIÇÃO: SOBREPESO')
elif bmi >= 18.5 and bmi < 25:
    print('CONDIÇÃO: PESO IDEAL')
else:
    print('CONDIÇÃO: ABAIXO DO PESO')