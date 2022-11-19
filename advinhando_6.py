from random import randint


def result(x, y):
    if x == y: return 'VOCÊ VENCEU'
    else: return 'ALTO' if x > y else 'BAIXO'


def nivel (a):
    if a == 1: return 10
    elif a == 2: return 100
    elif a == 3: return 1000


print('Seja bem-vindo a "ADIVINHANDO NUMS #6"')
print('1 = FÁCIL | 2 = MÉDIO | 3 = DIFÍCIL')
lvl = int(input('selecione o nível: '))

n = 0
num_sec = randint(1, nivel(lvl))
while n != num_sec:
    n = int(input('Digite um valor: '))
    print(result(n, num_sec))

print(f'número secreto = {num_sec}')
print('fim de jogo')