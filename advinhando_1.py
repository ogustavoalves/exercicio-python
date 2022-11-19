def resultado(i, c):
    if i == c: r = 'VOCÊ VENCEU'
    else: r = 'VOCÊ PERDEU'
    return r

# def nivel (a):
#     if a == 1: return 10
#     elif a == 2: return 100
#     elif a == 3: return 1000
#
#
# print('Seja bem-vindo a "ADIVINHANDO NUMS #1"')
# print('1 = FÁCIL | 2 = MÉDIO | 3 = DIFÍCIL')
# lvl = int(input('selecione o nível: '))

num_secreto = 33
num = int(input('digite um número: '))
print(resultado(num, num_secreto))
print('fim de jogo')
