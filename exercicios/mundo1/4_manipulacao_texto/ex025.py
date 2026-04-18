# Mais outro exercício sobre manipulação de strings

name = str(input('Digite seu nome: ')).lower().strip()

print('Seu nome possui Silva?', bool(name.find('silva')))