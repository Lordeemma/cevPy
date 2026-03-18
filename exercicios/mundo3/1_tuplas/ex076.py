# Penúltimo exercício sobre tuplas

product = ('Café', 'Sanduíche', 'Suco', 'Fatia de bolo')
price = (6, 9, 4, 3)

print('{:^30}'.format('-' * 30))
print('{:^30}'.format('TABELA DE PREÇOS'))
print('{:^30}'.format('-' * 30))
print('{:^18} | {:^8}'.format('NOME DO PRODUTO', 'PREÇO'))
print('{:^30}'.format('-' * 30))

for i, v in enumerate(product):
    print('{:<18} | R${:^6.2f}'.format(product[i], price[i]))

print('{:^30}'.format('-' * 30))