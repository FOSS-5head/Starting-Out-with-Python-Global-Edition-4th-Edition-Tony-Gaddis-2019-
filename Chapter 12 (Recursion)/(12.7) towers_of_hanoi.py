# Эта программа имитирует головоломку 'Ханойские башни'.


def main():
    # Задать несколько исходных значений.
    num_discs = 3
    from_peg = 1
    to_peg = 3
    temp_peg = 2

    # Решить головоломку.
    move_discs(num_discs, from_peg, to_peg, temp_peg)
    print('Все кольца перемещены!')


# Функция moveDiscs показывает процесс перемещения
# колец в головоломке 'Ханойские башни'.
# Параметры функции:
# num: количество перемещаемых колец.
# from_peg: стержень, с которого взять кольцо.
# to_peg: стержень, на который переложить кольцо.
# temp_peg: временный стержень.
def move_discs(num, from_peg, to_peg, temp_peg):
    if num > 0:
        move_discs(num - 1, from_peg, temp_peg, to_peg)
        print(f'Переложить кольцо с {from_peg} на {to_peg}')
        move_discs(num - 1, temp_peg, to_peg, from_peg)


# Вызвать главную функцию.
main()
