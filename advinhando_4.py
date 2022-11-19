from random import randint


def resultado(a, b):
    if a == b:
        return 'VOCÊ VENCEU'
    else:
        if a > b:
            return 'ALTO'
        else:
            return 'BAIXO'


print('Seja bem-vindo')

num_sec = randint(1, 100)
num = 0
while num != num_sec:
    num = int(input('Digite um número: '))
    print(resultado(num, num_sec))
print('fim de jogo')
