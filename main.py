import advinhando_1, advinhando_2, advinhando_3, advinhando_4, advinhando_5, advinhando_6

def escolha(a):
    print(f'jogando Advinhação #{a}')
    if a == 1: advinhando_1.jogar()
    elif a == 2: advinhando_2.jogar()
    elif a == 3: advinhando_3.jogar()
    elif a == 4: advinhando_4.jogar()
    elif a == 5: advinhando_5.jogar()
    else: advinhando_6.jogar()


print('=======================')
print('--Escolha seu Jogo--')
print('=======================')

for i in range (1, 7):
    print(f'Advinhação #{i}|')
n = int(input('sua escolha é:'))


if (__name__ == '__main__'):
    escolha(n)