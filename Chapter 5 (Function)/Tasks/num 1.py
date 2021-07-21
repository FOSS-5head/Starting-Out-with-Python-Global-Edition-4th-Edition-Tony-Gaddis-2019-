const = 0.6214


def main():
    km = float(input('Введите расстояние киллометров: '))
    miles = km * const
    print(format(miles, '.3f'), sep='')


main()
