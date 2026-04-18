# Último exercício sobre listas

parenthesis = []

exp = str(input('Digite uma expressão matemática: '))

for p in exp:
    if p == '(':
        parenthesis.append('(')
    elif p == ')':
        if len(parenthesis) > 0:
            parenthesis.pop()
        else:
            parenthesis.append(')')
            break

if len(parenthesis) == 0:
    print('Expressão válida!')
else:
    print('Expressão inválida!')
