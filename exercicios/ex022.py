# Exercício de manipulação de strings

name = str(input('Digite seu nome completo: ')).strip()

print('Seu nome em maiúsculo: {}'.format(name.upper()))
print('Seu nome em minúsculo: {}'.format(name.lower()))
print('Seu nome tem ao todo {} letras.'.format(len(name) - name.count(' ')))
print('Seu primeiro nome tem {} letras.'.format(len(name.split()[0])))
