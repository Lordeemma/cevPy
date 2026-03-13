# Exercício sobre módulos

from math import trunc

floating_point = float(input('Digite um número racional ou irracional: '))

print('A parte inteira de {:.10f} é {}'.format(floating_point, trunc(floating_point)))
