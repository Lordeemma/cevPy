def fatorial(num, key=0):
    '''
        => Calcula o fatorial de um número.
        :param num: O número a ser calculado;
        :param key: (opcional) Mostrar ou não o processo da conta; 
        :return: Não há retorno.
    '''
    f = 1

    if key == 0:
        for c in range(num, 1, -1):
            f *= c
        print(f'O fatorial de {num} é {f}')
    else:
        from time import sleep

        print(f'O fatorial de {num} é: ')
        for c in range(num, 0, -1):
            f *= c
            if c > 1:
                print(f'{c}', end=' * ', flush=True)
                sleep(0.4)
            else:
                print(f'{c} = {f}')

print('=' * 30)
fac = int(input('Número: '))
chave = int(input('0 para obter apenas o resultado, 1 para mostrar o processo do cálculo: '))
print('')
fatorial(fac, chave)