from modules import coin


def main():
    coin1 = coin.Coin()
    coin2 = coin.Coin()
    coin3 = coin.Coin()

    print('Вот три монеты у которых эти стороны обращены вверх:')
    print(coin1.get_sideup())
    print(coin2.get_sideup())
    print(coin3.get_sideup())
    print()

    print('Подбрасываю все три монеты...')
    print()
    coin1.toss()
    coin2.toss()
    coin3.toss()

    print('Теперь обращены вверх вот эти стороны:')
    print(coin1.get_sideup())
    print(coin2.get_sideup())
    print(coin3.get_sideup())
    print()


main()
