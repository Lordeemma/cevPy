from time import sleep

def pyHelp(funcao):

    print('\033[0;37;44m=' * 40)
    print(f'{f"Acessando o manual do comando '{funcao}'":^40}')
    print('=' * 40)
    print('\033[m')
    sleep(3)

    print('\033[7m', eval(funcao).__doc__)

while True:
    print('\033[0;37;42m=' * 30)
    print(f'{'SISTEMA DE AJUDA PYHELP':^30}')
    print('=' * 30)
    print('\033[m')
    escolha = input('Função ou Biblioteca > ').strip().lower()

    if escolha == 'FIM':
        print('\033[0;37;41m=' * 20)
        print(f'{'ATÉ LOGO':^20}')
        print('=' * 20)
        break
    else:
        pyHelp(escolha)