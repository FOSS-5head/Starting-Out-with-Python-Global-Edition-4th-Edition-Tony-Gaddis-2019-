def main():
    def range_sum(data):
        seq, params = data
        fn = lambda start, end: 0 if start > end \
            else seq[start] + fn(start + 1, end)

    def indata():
        seq = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        params = (2,5)
        return seq, params

    def outdata():
        def f(data):
            msg = 'Сумма значений со 2 по 5 позициб равняется'
            print(msg, format(data), sep='')

        return f

    pipe(indata(), range_sum, outdata())


main()
