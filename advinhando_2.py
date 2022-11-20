def jogar():
    print('-------------------------------')
    print('Seja bem-vindo a ADVINHAÇÃO #2')
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

    print(resultado(num, num_sec))

if (__name__ == '__main__'):
    jogar()