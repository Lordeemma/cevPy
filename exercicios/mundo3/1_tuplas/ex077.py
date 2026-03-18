# Último exercício sobre tuplas

words = ('amar', 'praticar', 'estudo', 'python', 'livro', 'bloco')

for index, w in enumerate(words):

    word = words[index].lower()
    print('Na palavra {} temos'.format(words[index].upper()), end=' ')
    
    for vpos in range(0, len(word)):

        vowel = 0

        if word[vpos] == 'a':
            vowel = 'a'
        elif word[vpos] == 'e':
            vowel = 'e'
        elif word[vpos] == 'i':
            vowel = 'i'
        elif word[vpos] == 'o':
            vowel = 'o'
        elif word[vpos] == 'u':
            vowel = 'u'
        else:
            continue

        print(vowel, end=' ')

    print('')