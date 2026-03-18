# Mais outro exercício sobre tuplas

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite mais um número: '))
n4 = int(input('Digite o último número: '))

tuple = (n1, n2, n3, n4)
even_c = 0

print(f'Você digitou os valores {tuple}')
print(f'O valor 9 apareceu {tuple.count(9)} vezes')

for i, n in enumerate(tuple):

    if n == 3:
        print(f'O valor 3 apareceu na {i + 1}ª posição')

for even in range(0, len(tuple)):

    number = int(tuple[even])

    if number % 2 == 0:
        even_c += 1

print(f'Valores pares na tupla: {even_c}')