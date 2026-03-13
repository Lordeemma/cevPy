# Outro exercício relacionado a operações aritméticas

height = float(input('Insira a altura de uma parede em metros: '))
length = float(input('Insira a largura de uma parede em metros:'))
area = height * length
paint = area / 2

print('Sua parede possui {}m. Para pintar sua parede, serão necessários {:.2f}L de tinta.'.format(area, paint))
