# Outro exercício sobre módulos

from math import cos, sin, tan, radians

degree = float(input('Insira o valor de um ângulo: '))

print('Seno de {}°: {:.2f}'.format(degree, sin(radians(degree))))
print('Cosseno de {}°: {:.2f}'.format(degree, cos(radians(degree))))
print('Tangente de {}°: {:.2f}'.format(degree, tan(radians(degree))))