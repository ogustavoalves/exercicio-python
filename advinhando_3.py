print('Seja bem-vindo')


def resultado(a, b):
    if a == b:
        return 'VOCÊ VENCEU'
    else:
        if a > b:
            return 'ALTO'
        else:
            return 'BAIXO'


num = 0
num_sec = 33
while num != 33:
    num = int(input('Digite um número: '))
    print(resultado(num, num_sec))
