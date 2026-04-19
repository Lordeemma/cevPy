from time import sleep

def lin():
    print('-=' * 20)

def contador(start, end, step):

    print(f'Contagem de {start} até {end} de {abs(step)} em {abs(step)}')
    for i in range(start, end, step):
        if start < end:
            print(f'{i + 1}', end=' ', flush=True)
        elif start > end:
            print(f'{i}', end=' ', flush=True)
        sleep(0.3)
    print('FIM!')

lin()
print('Contagem de 1 até 10 de 1 em 1')
for i in range(0, 10):
    print(f'{i + 1}', end=' ', flush=True)
    sleep(0.3)
print('FIM!')
lin()
print('Contagem de 10 até 0 de 2 em 2')
for i in range(10, 0, -2):
    print(f'{i}', end=' ', flush=True)
    sleep(0.3)
print('FIM!')
lin()

print('Agora é sua vez de personalizar a contagem!')
inicio = int(input(f'{'Início: ':<8}'))
fim = int(input(f'{'Fim: ':<8}'))
passo = int(input(f'{'Passo: ':<8}'))

if passo == 0:
    passo = 1

if inicio > fim:
    passo = -passo

lin()
contador(inicio, fim, passo)