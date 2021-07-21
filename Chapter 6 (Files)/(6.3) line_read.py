# Эта программа построчно читает
# содержимое файла (6.1)philosophers.txt.


def main():
    # Открыть файл с именем philosophers.txt.
    infile = open('(6.1)philosophers.txt', 'r')

    # Прочитать три строки файла.
    line1 = infile.readline()
    line2 = infile.readline()
    line3 = infile.readline()

    # Закрыть файл.
    infile.close()

    # Напечатать данные, прочие данные
    # в оперативную память.
    print(line1)
    print(line2)
    print(line3)


# Вызвать главную функцию.
main()
