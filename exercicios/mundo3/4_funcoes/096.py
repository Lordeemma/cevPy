def calcArea(lgr, cmp):
    area = lgr * cmp
    print(f'A área de um terreno {lgr}x{cmp} é de {area}m²')

print('Controle de terrenos')
print('=' * 20)

largura = float(input('LARGURA (m): '))
comprimento = float(input('COMPRIMENTO (m): '))
calcArea(largura, comprimento)