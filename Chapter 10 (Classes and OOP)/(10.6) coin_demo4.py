from modules import coin


def main():
    my_coin = coin.Coin()
    print('Эта сторона обращена вверх', my_coin.get_sideup())

    print('Собираюсь подбросить монету десять раз:')
    for count in range(10):
        my_coin.toss()
        print(my_coin.get_sideup())


main()
