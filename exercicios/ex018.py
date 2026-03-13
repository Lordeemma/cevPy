# Outro exercício sobre módulos

from math import cos, sin, tan

degree = float(input('Insira o valor de um ângulo: '))

print('Seno de {}°: {}'.format(degree, sin(degree)))
print('Cosseno de {}°: {}'.format(degree, cos(degree)))
print('Tangente de {}°: {}'.format(degree, tan(degree)))