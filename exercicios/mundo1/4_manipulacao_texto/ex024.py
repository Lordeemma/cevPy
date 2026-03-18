# Outro exercício sobre manipulação de strings

city_name = str(input('Insira o nome de uma cidade: ')).lower().strip().split()

print('Sua cidade possui "Santo" no início do nome?', bool('santo' in city_name[0]))
