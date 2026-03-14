# Mais outro exercício sobre manipulação de strings

name = str(input('Digite seu nome: ')).lower().strip()

print('Seu nome possui Silva?')
if name.find('silva') != -1:
   print('SIM')
else:
   print('NÃO')