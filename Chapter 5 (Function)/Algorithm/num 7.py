total = float(input('Введите любое число: '))


def main():
    result = half(total)
    print(result)


def half(a):
    a /= 2
    return a


main()
