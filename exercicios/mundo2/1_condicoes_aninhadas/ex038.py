# Mais outro exercício sobre condições aninhadas

n1 = int(input('Insira o primeiro número inteiro: '))
n2 = int(input('Insira o segundo número inteiro:'))

if n1 > n2:
    print('O primeiro valor ({}) é maior.'.format(n1))
elif n2 > n1:
    print('O segundo valor ({}) é maior.'.format(n2))
else:
    print('Os números são idênticos.')
