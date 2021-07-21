# Эта программа "бросает" кубики.
import random
import time

# Константы для минимального и максимального случайных чисел
MIN = 1
MAX = 6


def main():
    # Создать переменную, которая управляет циклом.
    again = 'д'

    # Имитировать бросание кубиков.
    while again == 'д' or again == 'д':
        print('Бросаем кубики ... ')
        time.sleep(2)
        print('Значения граней:')
        print(random.randint(MIN, MAX))
        print(random.randint(MIN, MAX))

        # Сделать еще один бросок кубиков?
        again = input('Бросить кубики еще раз? (д = да): ')


# Вызвать главную функцию.
main()
