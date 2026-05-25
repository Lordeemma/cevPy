def menuPrincipal():
    print("\033[2J\033[H", end="")
    print('-' * 50)
    print(f'{"MENU PRINCIPAL":^50}')
    print('-' * 50)

    print('\033[0;33m1\033[m - \033[0;34mVer pessoas cadastradas')
    print('\033[0;33m2\033[m - \033[0;34mCadastrar nova pessoa')
    print('\033[0;33m3\033[m - \033[0;34mSair do sistema\033[m')
    print('-' * 50)

    try:
        n = int(input('\033[0;33mSua Opção:\033[m \033[0;32m\033[m'))

        if n <= 0 or n > 3:
            print('\033[0;31mERRO: Digite uma opção válida!\033[m')
        else:
            print("\033[2J\033[H", end="")
            return n
    except ValueError:
        print('\033[0;31mERRO: Digite uma opção válida!\033[m')
    except KeyboardInterrupt:
        n = 3
        print('')
        return n

def novoCadastro():
    print("\033[2J\033[H", end="")
    print('-' * 50)
    print(f'{"NOVO CADASTRO":^50}')
    print('-' * 50)

def pessoasCadastradas():
    print("\033[2J\033[H", end="")
    print('-' * 50)
    print(f'{"NOVO CADASTRO":^50}')
    print('-' * 50)

def saida():
    print('-' * 50)
    print(f'{"Saindo do sistema... Até logo!":^50}')
    print('-' * 50)

def confirmar():
    n = input('')
