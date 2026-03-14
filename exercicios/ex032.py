# Outro exercício sobre condições

year = int(input('Digite um ano: '))

if year % 4 == 0 and year % 100 != 0:
    print('O ano {} é bissexto.'.format(year))
elif year % 4 == 0 and year % 400 == 0:
    print('O ano {} é bissexto.'.format(year))
else:
    print('O ano {} não é bissexto.'.format(year))