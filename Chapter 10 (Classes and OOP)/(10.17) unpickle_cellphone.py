import pickle

FILENAME = '(10.16) cellphones.dat'


def main():
    end_of_file = False  # Дпя обозначения конца файла

    # Открыть файл.
    with open(FILENAME, 'rb') as input_file:

        # Прочитать до конца файла.
        while not end_of_file:
            try:
                # Расконсервировать следу!СЩИЙ объект.
                phone = pickle.load(input_file)

                # Показать данные о сотовом телефоне.
                display_data(phone)

            except EOFError:
                # Установить флаг, чтобы обозначить, что
                # был достигнут конец файла.
                end_of_file = True


# Функция display_data показывает данные
# из объекта CellPhone, переданного в качестве аргумента.
def display_data(phone):
    print('Производитель: ', phone.get_manufact())
    print('Номер модели: ', phone.get_model())
    print('Розничная цена: $',
          format(phone.get_retail_price(), ',.2f'),
          sep=' ')
    print()


# Вызвать главную функцию.
main()
