def notas(*nota, sit=False):
    from math import inf

    aluno = dict()

    maior = 0
    menor = inf
    total = len(nota)
    soma = 0

    for i in range(len(nota)):
        soma += nota[i]

        if nota[i] > maior:
            maior = nota[i]
        if nota[i] < menor:
            menor = nota[i]

    media = soma / total

    aluno['total'] = total
    aluno['maior'] = maior
    aluno['menor'] = menor
    aluno['média'] = media

    if sit == True:
        if media >= 7:
            aluno['situação'] = 'BOA'
        elif media < 7 and media >= 5:
            aluno['situação'] = 'RAZOÁVEL'
        else:
            aluno['situação'] = 'RUIM'

    return aluno

print(notas(2, 3, 5, 7, sit=True))