def criarPessoa(nome, idade, db):
    import json

    pessoa = dict()

    while True:
        try:
            nome_pessoa = input(nome + '\033[0;32m').strip()
            
            if nome_pessoa != '' and all(c.isalpha() or c.isspace() for c in nome_pessoa):
                pessoa['nome'] = nome_pessoa

                while True:
                    try:
                        n = int(input('\033[m' + idade + '\033[0;32m'))
                        pessoa['idade'] = n
                        break
                    except ValueError:
                        print('\033[1;31mERRO: Por favor, digite um número inteiro válido.\033[m')
                    except KeyboardInterrupt:
                        print('\n\033[1;31mOperação cancelada.\033[m')
                        return
                break
            else:
                print('\033[1;31mERRO: O nome digitado não é válido.\033[m')
        except KeyboardInterrupt:
            print('\n\033[1;31mOperação cancelada.\033[m')
            return

    try:    
        with open(db, 'r', encoding='utf-8') as file:
            data = json.load(file)

        data.append(pessoa)

        with open(db, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
    except FileNotFoundError:
        print('\033[1;31mERRO: Banco de dados não encontrado.\033[m')
        return

    print(f'Novo registro de {nome_pessoa} adicionado.')

def lerPessoas(db):
    import json

    try:
        data = json.load(open(db, 'r'))
    except FileNotFoundError:
        print('\033[1;31mERRO: Banco de dados não encontrado.\033[m')
        return
    else:
        for i in range(len(data)):
            print(f'{data[i]["nome"]:<40} {f"{data[i]["idade"]} anos":>8}')
        print('-' * 50)

