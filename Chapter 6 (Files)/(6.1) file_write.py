# Эта программа пишет три строки данных
# в файл.


def main():
    # Открыть файл с именем philosophers.txt.
    outfile = open('(6.1)philosophers.txt', 'w')

    # Записать имена трех философов
    # в файл.
    outfile.write('Джoн Локк\n')
    outfile.write('Дэвид Хьюм\n')
    outfile.write('Эдмyнд Берк\n')

    # Закрыть файл.
    outfile.close()


# Вызвать главную функцию.
main()
