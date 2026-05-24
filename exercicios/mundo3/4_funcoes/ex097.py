def escreva(txt):
    print('=' * (len(txt) + 10))
    print(f'{txt:^{len(txt) + 10}}')
    print('=' * (len(txt) + 10))

escreva(str(input('Digite um texto: ')))
