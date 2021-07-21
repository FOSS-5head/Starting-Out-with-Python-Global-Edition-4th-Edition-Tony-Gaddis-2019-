# Эта программа читает и показывает содержимое
# файла philosophers.txt.


def main():
    # Открыть файл с именем philosophers.txt.
    infile = open('(6.1)philosophers.txt', 'r')

    # Прочитать содержимое файла.
    file_contents = infile.read()

    # Закрыть файл.
    infile.close()

    # Напечатать данные, считанные
    # в оперативную память.
    print(file_contents)


# Вызвать главную функцию.
main()
