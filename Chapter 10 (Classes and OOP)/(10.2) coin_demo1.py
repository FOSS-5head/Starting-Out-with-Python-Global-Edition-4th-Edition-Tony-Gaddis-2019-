from random import randint


class Coin:
    def __init__(self):
        self.sideup = 'Орел'

    def toss(self):
        if randint(0, 1) == 0:
            self.sideup = 'Орел'
        else:
            self.sideup = 'Решка'

    def get_sideup(self):
        return self.sideup


def main():
    my_coin = Coin()

    print('Эта сторона обращена вверх:', my_coin.get_sideup())

    print('Подбрасываю монету...')
    my_coin.toss()
    print('Эта сторона обращена вверх:', my_coin.get_sideup())


main()
