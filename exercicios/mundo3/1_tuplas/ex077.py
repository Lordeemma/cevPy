# Último exercício sobre tuplas

words = ('amar', 'praticar', 'estudo', 'python', 'livro', 'bloco')

for w in words:

    word = w.lower()
    print('Na palavra {} temos'.format(w.upper()), end=' ')
    
    for vpos in w:

        if vpos in 'aeiou':
            print(vpos, end=' ')
        else:
            continue

    print('')