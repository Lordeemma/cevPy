# Mais outro exercício sobre condições aninhadas

l1 = float(input('Insira o tamanho da primeira reta: '))
l2 = float(input('Insira o tamanho da segunda reta: '))
l3 = float(input('Insira o tamanho da terceira reta: '))

if l1 > l2 + l3 or l2 > l1 + l3 or l3 > l1 + l2:
    print('Não é possível formar um triângulo.')
else:
    print('É possível formar um triângulo')
    if l1 == l2 and l1 == l3:
        print('O triângulo é equilátero')
    elif l1 == l2 and l1 != l3 or l2 == l3 and l2 != l1 or l3 == l1 and l3 != l2:
        print('O triângulo é isósceles.')
    elif l1 != l2 and l1 != l3 and l2 != l3:
        print('O triângulo é escaleno.')
        