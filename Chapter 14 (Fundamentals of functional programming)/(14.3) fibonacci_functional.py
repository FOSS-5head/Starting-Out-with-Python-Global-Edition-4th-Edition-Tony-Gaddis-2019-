from functools import reduce


def pipe(data, *fseq):
    for fn in fseq:
        data = fn(data)
    return data


def main():
    def fibonacci(n, x=0, y=1):
        fib = lambda n, x=0, y=1: x if n <= 0 else fib(n - 1, y, x + y)
        acc = []
        reduce(lambda _, y: acc.append(fib(y)), range(n+1))
        return n, acc

    def validate(n):
        if not isinstance(n, int):
            raise TypeError('Число должно быть целым.')
        if not n >= 0:
            raise ValueError('Число должно быть нулем или положительным.')
        if n > 10:
            raise ValueError('Число должно быть не больше 10.')
        return n

    def indata():
        msg = 'Введите неотрицательное целое число не больше 10: '
        return pipe(get_int(msg), validate)

    def outdata():
        def fn(data):
            n, seq = data
            msg = f'Первые {n} чисел последовательности Фибоначчи:'
            print(msg)
            [print(el) for el in seq]
        return fn

    pipe(indata(), fibonacci(), outdata())


main()
