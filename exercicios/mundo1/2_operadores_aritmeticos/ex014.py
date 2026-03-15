# Penúltimo exercício sobre operações aritméticas

celsius = float(input('Insira a temperatura em graus Celsius: '))
fahrenheit = float(input('Insira a temperatura em graus Fahrenheit: '))
ctf = (celsius * 9/5) + 32
ftc = (fahrenheit - 32) * 5/9

print('Celsius para Fahrenheit: {:.2f}°F'.format(ctf))
print('Fahrenheit para Celsius: {:.2f}°C'.format(ftc))