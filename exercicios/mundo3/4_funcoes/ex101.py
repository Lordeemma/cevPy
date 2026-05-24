def voto(ano):
    from datetime import date
    idade = date.today().year - ano
    voto = 0

    if idade < 16:
        voto = 'NEGADO'
    elif idade >= 16 and idade < 18 or idade > 70:
        voto = 'OPCIONAL'
    elif idade >= 18 and idade < 70:
        voto = 'OBRIGATÓRIO'

    print(f'Com {idade} anos: voto {voto}')
    
print('=' * 20)
ano = int(input('Em que ano você nasceu? '))
voto(ano)

