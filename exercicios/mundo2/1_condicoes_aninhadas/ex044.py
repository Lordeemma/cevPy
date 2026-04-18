# Penúltimo exercício sobre condições aninhadas

price = float(input('Insira o valor do produto: R$'))
payment_method = int(input("""
    Qual será o método de pagamento?
    [1] À vista em dinheiro/talão de cheque
    [2] Á vista no cartão                    
    [3] Em até duas parcelas
    [4] Três ou mais parcelas                  
    """))

if payment_method == 1:
    print('Um desconto de 10% foi aplicado. O valor do produto agora é R${:.2f}.'.format(price - (price * 0.1)))
elif payment_method == 2:
    print('Um desconto de 5% foi aplicado. O valor do produto agora é R${:.2f}.'.format(price - (price*0.05)))
elif payment_method == 3:
    print('O preço íntegro de {} foi cobrado.'.format(price))
elif payment_method == 4:
    print('Um juros de 20% foi aplicado. O preço do produto agora é R${}.'.format(price + (price * 0.2)))