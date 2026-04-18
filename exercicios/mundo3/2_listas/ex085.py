lista_numeros = [[], []]

for i in range(1, 8):
    n = int(input(f'Digite o {i}º número: '))

    if n % 2 == 0:
        lista_numeros[0].append(n)
    else:
        lista_numeros[1].append(n)

lista_numeros[0].sort()
lista_numeros[1].sort()

print(f'Números pares: {lista_numeros[0]}')
print(f'Números ímpares: {lista_numeros[1]}')

