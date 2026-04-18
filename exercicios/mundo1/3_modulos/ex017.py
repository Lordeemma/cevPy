# Mais um exercício sobre módulos

from math import hypot

cathet_o = float(input('Insira o valor do cateto oposto: '))
cathet_a = float(input('Insira o valor do cateto adjacente:'))
_hypot = hypot(cathet_o, cathet_a)

print('A hipotenusa é {}'.format(_hypot))
