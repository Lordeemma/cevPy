# Exercício sobre o laço while

gender = ''

while gender != 'h' and gender != 'f':
    g = str(input('Qual é seu gênero [H/F]? ')).lower()
    
    if g == 'h':
        gender = 'h'
    
    if g == 'f':
        gender = 'f'

    if g != 'h' and g != 'f':
        print('Digite uma opção válida!')