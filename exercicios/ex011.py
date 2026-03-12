# Outro exercício relacionado a operações aritméticas

height = float(input('Insira a altura de uma parede em metros: '))
length = float(input('Insira a largura de uma parede em metros:'))
area_paint = (height * length) / 2

print('Para pintar sua parede, serão necessários {:.2f}L de tinta.'.format(area_paint))
