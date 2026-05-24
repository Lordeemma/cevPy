from time import sleep

def lin():
    print('-=' * 20)


def maiorNum(* num):
    maior = 0

    lin()
    print('Analisando os dados passados...')
    for i in num:

        if i > maior:
            maior = i
        print(i, end=' ', flush=True)
        sleep(0.5)
    print(f'foram informados {len(num)} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')

maiorNum(2, 9, 4, 5, 7, 1)
maiorNum(4, 7, 0)
maiorNum(1, 2)
maiorNum(6)
maiorNum()

    

    

    