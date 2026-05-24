def leiaint(msg):
    while True:
        try:
            valor = int(input(msg))
            return valor
        except ValueError:
            print('\033[1;31mERRO! Por favor, digite um número inteiro válido!\033[m')
        except KeyboardInterrupt:
            print('')
            print('\033[1;31mO usuário preferiu não digitar este número.\033[m')
            return 0


def leiafloat(msg):
    while True:
        try:
            valor = float(input(msg))
            return valor
        except ValueError:
            print('\033[1;31mERRO! Por favor, digite um número real válido!\033[m')
        except KeyboardInterrupt:
            print('')
            print('\033[1;31mO usuário preferiu não digitar este número.\033[m')
            return 0

inteiro = leiaint('Digite um número inteiro: ')
decimal = leiafloat('Digite um número real: ')
print(f'O número inteiro digitado foi {inteiro} e o número real foi {decimal}.')