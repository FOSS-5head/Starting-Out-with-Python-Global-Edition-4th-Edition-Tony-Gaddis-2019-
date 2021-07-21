def main():
    found = False
    search = input('Введите искомое описание: ')
    coffee_file = open('(6.15)coffee.txt', 'r')
    descr = coffee_file.readline()

    while descr != '':
        qty = float(coffee_file.readline())
        descr = descr.rstrip('\n')
        if descr == search:
            print('Описание:', descr)
            print('Количество:', qty)
            print()

            found = True
        descr = coffee_file.readline()

    coffee_file.close()

    if not found:
        print('Это значение в файле не найдено.')


main()
