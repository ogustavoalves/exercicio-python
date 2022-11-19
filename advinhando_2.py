print('Seja Bem-Vindo')
def resultado(a, b):
    if a == b:
        return 'VOCÊ VENCEU'
    else:
        if a > b:
            return 'ALTO'
        else:
            return 'BAIXO'

num = int(input('Digite um número:'))
num_sec = 33

print(resultado(num,num_sec))