# Outro exercício sobre operações aritméticas

price = float(input('Insira o valor de um produto: '))
price_discount = price - ((price * 5) / 100)

print('O valor do produto com um desconto de 5% é de R${}'.format(price_discount))
