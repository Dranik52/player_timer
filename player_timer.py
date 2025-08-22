from time import *

def player(num):
    start = time()
    input(f'Игрок {num}, нажми Enter, когда захочешь остановиться...')
    stop = time()
    return stop - start

who = input('Начать игру? (да/стоп): ')

while who != 'стоп':
    if who == 'да':
        proshlo1 = player(1)
        print('Игрок 1 прошло:', round(proshlo1), 'сек')

        who = input('Следующий игрок? (да/стоп): ')
        if who == 'да':
            proshlo2 = player(2)
            print('Игрок 2 прошло:', round(proshlo2), 'сек')

        who = input('Ещё раз? (да/стоп): ')
