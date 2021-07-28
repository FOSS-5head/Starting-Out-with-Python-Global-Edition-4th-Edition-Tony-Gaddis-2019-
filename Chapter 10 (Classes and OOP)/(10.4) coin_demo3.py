import random


class Coin:
    def __init__(self):
        self.__sideup = 'Орел'

    def toss(self):
        if random.randint(0, 1) == 0:
            self.__sideup = 'Орел'
        else:
            self.__sideup = 'Решка'

    def get_sideup(self):
        return self.__sideup


def main():
    my_coin = Coin()
    print('Эта сторона обращена вверх:', my_coin.get_sideup())

    print('Собираюсь подбросить монету десят раз:')
    for count in range(10):
        my_coin.toss()
        print(my_coin.get_sideup())


main()
