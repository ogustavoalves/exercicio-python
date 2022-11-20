def jogar ():
    print('-------------------------------')
    print('Seja bem-vindo a ADVINHAÇÃO #1')
    def resultado(i, c):
        if i == c: r = 'VOCÊ VENCEU'
        else: r = 'VOCÊ PERDEU'
        return r


    num_secreto = 33
    num = int(input('digite um número: '))
    print(resultado(num, num_secreto))
    print('fim de jogo')

if(__name__ == '__main__'):
    jogar()