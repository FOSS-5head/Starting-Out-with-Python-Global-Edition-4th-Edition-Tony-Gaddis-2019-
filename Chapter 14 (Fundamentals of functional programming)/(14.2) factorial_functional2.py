# Эта программа демонстрирует
# функциональную версию функции factorial из главы 12

import functools


def pipe(data, *fseq):
    for fn in fseq:
        data = fn(data)
    return data


def get_int(msg=''):
    return int(input(msg))


def main():
    def factorial_rec(n):
        fn = lambda n, acc=1: acc if n == 0 else fn(n-1, acc * n)
        return n, fn(n)

    def factorial(n):
        return n, reduce(lambda x, y: x * y, range(1, n+1))

    def indata():
        def validate(n):
            if not isinstance(n, int):
                raise TypeError('Число должно быть целым.')
            if not n >= 0:
                raise ValueError('Число должно быть >= 0.')
            return n
        msg = 'Введите неотрицательное целое число: '
        return pipe(get_int(msg), validate)

    def outdata():
        def fn(data):
            n, fact = data
            print(f'Факториал числа {n} равняется {fact}')
        return fn

    pipe(indata(),
         factorial,
         outdata())


main()
