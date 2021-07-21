number = float(input('Введите значение: '))


def main():
    result = times_ten(number)
    print(result)


def times_ten(a):
    a *= 10
    return a


main()
