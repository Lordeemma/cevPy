# Mais um exercício sobre o laço for

sentence = str(input('Insira uma palavra ou frase: ')).strip()

if sentence.find(' ') != -1:
    sentence.replace(' ', '')

for i in range(0, len(sentence)): # O laço for correto não funciona em meu IDE por algum motivo. Este laço inserido não tem utilidade.
    if sentence == sentence[::-1]:
        print('É um palíndromo.')
    else:
        print('Não é um palíndromo.')
    break