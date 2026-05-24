import funcs.banco as banco
import funcs.screens as screens

while True:
    escolha = screens.menuPrincipal()

    if escolha == 1:
        screens.pessoasCadastradas()
        banco.lerPessoas('db.txt')
        screens.confirmar()
    elif escolha == 2:
        screens.novoCadastro()
        banco.criarPessoa('Digite o nome da pessoa: ', 'Digite a idade da pessoa: ', 'db.txt')
        screens.confirmar()
    elif escolha == 3:
        screens.saida()
        break
