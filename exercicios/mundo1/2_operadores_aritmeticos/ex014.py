# Penúltimo exercício sobre operações aritméticas

celsius = float(input('Insira a temperatura em graus Celsius: '))
fahrenheit = float(input('Insira a temperatura em graus Fahrenheit: '))
celsius_to_fahrenheit = (celsius * 9/5) + 32
fahrenheit_to_celsius = (fahrenheit - 32) * 5/9

print('Celsius para Fahrenheit: {:.2f}°F'.format(celsius_to_fahrenheit))
print('Fahrenheit para Celsius: {:.2f}°C'.format(fahrenheit_to_celsius))