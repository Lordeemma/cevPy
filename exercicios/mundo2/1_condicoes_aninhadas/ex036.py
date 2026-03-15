# Exercício sobre condições aninhadas

house_value = float(input('Insira o valor do imóvel: R$'))
wage = float(input('Insira o valor do seu salário: R$'))
installment = int(input('Em quantos anos você irá pagar o empréstimo? '))
loan = house_value / (installment * 12)

if loan > (wage * 0.3):
    print('Empréstimo negado.')
else:
    print('Empréstimo aprovado.')