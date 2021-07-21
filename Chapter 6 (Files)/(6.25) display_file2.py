# Эта программа показывает содержимое
# файла.


def main():
    # Получить имя файла.
    filename = input('Введите имя файла: ')

    try:
        # Открыть файл.
        infile = open(filename, 'r')

        # Прочитать содержимое файла.
        contents = infile.read()

        # Показать содержимое файла.
        print(contents)

        # Закрыть файл.
        infile.close()

    except IOError:
        print('Произошла ошибка при попытке прочитать')
        print('файл \'', filename, '\'!', sep='')


# Вызвать главную функцию.
main()
