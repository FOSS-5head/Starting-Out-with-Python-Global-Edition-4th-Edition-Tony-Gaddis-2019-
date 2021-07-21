# Эта программа считывает содержимое файла в список.


def main():
    # Открыть файл для чтения.
    infile = open('(7.14) cities.txt', 'r')

    # Прочитать содержимое файла в список.
    cities = infile.readlines()

    # Закрыть файл.
    infile.close()

    # Удалить из каждого элемента символ \n.
    index = 0
    while index < len(cities):
        cities[index] = cities[index] .rstrip('\n')
        index += 1

    # Напечатать содержимое списка.
    print(cities)


# Вызвать главную функцию.
main()
