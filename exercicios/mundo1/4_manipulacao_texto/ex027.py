# Último exercício sobre manipulação de strings

name = str(input('Digite seu nome completo: ')).strip()
split_name = name.split()

print('Primeiro nome: {}'.format(split_name[0]))
print('Último nome: {}'.format(split_name[-1]))