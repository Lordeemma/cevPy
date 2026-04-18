import datetime

cadastro = dict()

cadastro['nome'] = str(input('Nome: '))
cadastro['idade'] = datetime.date.today().year - int(input('Ano de nascimento: '))
cadastro['ctps'] = int(input('Carteira de trabalho (0 não tem): '))

if cadastro['ctps'] != 0:
    cadastro['contratação'] = int(input('Ano de contratação: '))
    cadastro['salário'] = float(input('Salário: '))
    cadastro['aposentadoria'] = cadastro['idade'] + (35 - (datetime.date.today().year - cadastro['contratação']))

print('-=' * 30)
print(cadastro)
for k, v in cadastro.items():
    print(f'{k} tem o valor {v}')

