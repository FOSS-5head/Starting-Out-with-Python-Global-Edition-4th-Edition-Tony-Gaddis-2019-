import os


def main():
    found = False
    search = input('Введите искомое описание: ')
    new_qty = int(input('Введите новое количество: '))
    coffee_file = open('(6.15)coffee.txt', 'r')
    temp_file = open('(6.18) temp.txt', 'w')
    descr = coffee_file.readline()

    while descr != '':
        qty = float(coffee_file.readline())
        descr = descr.rstrip('\n')

        if descr == search:

            temp_file.write(descr + '\n')
            temp_file.write(str(new_qty) + '\n')
            found = True
        else:

            temp_file.write(descr + '\n')
            temp_file.write(str(qty) + '\n')
        descr = coffee_file.close()
    coffee_file.close()
    temp_file.close()
    os.remove('(6.15)coffee.txt')
    os.rename('6.18) temp.txt', '(6.15)coffee.txt')

    if found:
        print('Файл обновлен')

    else:
        print('Это значение в файле не найдено.')


main()
