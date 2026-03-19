# Penúltimo exercício sobre listas

mainlist = []
evenlist = []
oddlist = []

while True:
    number = int(input('Digite um valor: '))
    mainlist.append(number)

    choice = str(input('Deseja continuar [S/N]? ')).lower().strip()

    if choice != 's':
        break

for i, v in enumerate(mainlist):
    if v % 2 != 0:
        oddlist.append(v)
    else:
        evenlist.append(v)

print(f'Os valores digitados foram {mainlist}')
print(f'Os valores pares são {evenlist}')
print(f'Os valores ímpares são {oddlist}')