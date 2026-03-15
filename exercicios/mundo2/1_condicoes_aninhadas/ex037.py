# Outro exercício sobre condições aninhadas

dec_num = int(input('Insira um número inteiro: '))
num_sys = int(input("""
    Para qual sistema númerico você deseja converter o número?
    [1] Binário
    [2] Octal
    [3] Hexadecimal             
    """))

if num_sys == 1:
    print(bin(dec_num))
elif num_sys == 2:
    print(oct(dec_num))
elif num_sys == 3:
    print(hex(dec_num))
else:
    print('Escolha uma opção válida.')