# Mais um exercício sobre módulos

from math import hypot

cat_o = float(input('Insira o valor do cateto oposto: '))
cat_a = float(input('Insira o valor do cateto adjacente:'))
_hypot = hypot(cat_o, cat_a)

print('A hipotenusa é {}'.format(_hypot))
