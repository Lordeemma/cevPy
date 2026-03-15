# Outro exercício sobre manipulação de strings

city_name = str(input('Insira o nome de uma cidade: ')).lower().strip()

print('Sua cidade possui "Santo" no início do nome?')

if city_name.find('santo'.split()[0]) == 0:
    print('SIM')
else:
    print('NÃO')
