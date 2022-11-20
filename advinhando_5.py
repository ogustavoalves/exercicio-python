def jogar():

    from random import randint
    print('-------------------------------')
    print('Seja bem-vindo a ADVINHAÇÃO #5')
    def resultado(a, b):
        if a == b:
            return f'Acertou o número {b}'
        else:
            return 'Alto' if a > b else 'Baixo'


    n = 0
    num_sec = randint(1, 100)
    while n != num_sec:
        n = int(input('Digite um número:'))
        print(resultado(n, num_sec))
    print('Fim  de Jogo')

if (__name__ == '__main__'):
    jogar()