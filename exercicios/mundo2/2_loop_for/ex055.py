# Penúltimo exercício sobre o laço for

g_weight = 0
l_weight = 1000

for i in range(1, 5 + 1):
    weight = float(input('Insira o peso da {}ª pessoa: '.format(i)))

    if weight > g_weight:
        g_weight = weight
    elif weight < g_weight and weight < l_weight:
        l_weight = weight

print('Maior peso: {}kg'.format(g_weight))
print('Menor peso: {}kg'.format(l_weight))
