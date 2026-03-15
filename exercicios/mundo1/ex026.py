# Penúltimo exercício sobre manipulação de strings

sentence = str(input('Insira uma frase: ')).lower()
a_count = int(sentence.count('a'))

print('a letra "A" aparece {} vezes'.format(a_count))
print('a letra "A" aparece, pela primeira vez, na posição {}'.format(sentence.find('a')))
print('a letra "A" aparece, pela última vez, na posição {}'.format(sentence.rfind('a')))