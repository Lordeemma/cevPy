# Mais um exercício envolvendo operações aritméticas

balance = float(input('Quantos reais você possui em saldo? '))
dollar_conversion = balance / 3.27

print('Seu saldo de R${:.2f} pode ser convertido em US${:.2f}'.format(balance, dollar_conversion))