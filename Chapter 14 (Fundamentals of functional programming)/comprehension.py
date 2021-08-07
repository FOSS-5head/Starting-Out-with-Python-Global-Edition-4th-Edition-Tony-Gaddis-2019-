# Программа показывает "включение в последовательность".


# Первый пример.
def first_ex():
    num = [1, 2, 3, 4, 5]
    squared_num = [x*x for x in num]
    print(squared_num)


# Второй пример.
def second_ex():
    seq = (1, 2, 3, 4, 5, 6, 7, 8, 9)
    seq2 = (5, 6, 7, 8, 9, 0, 3, 2, 1)
    result = [x + y for x, y in zip(seq, seq2)]
    print(result)

