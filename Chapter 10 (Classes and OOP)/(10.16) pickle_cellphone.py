import pickle
from modules import cellphone

FILENAME = '(10.16) cellphones.dat'


def main():
    again = 'д'

    with open(FILENAME, 'wb') as output_file:
        while again.lower() == 'д':
            man = input('Введите производителя: ')
            mod = input('Ввдите номер модели: ')
            retail = float(input('Введите розничную цену: '))

            phone = cellphone.CellPhone(man, mod, retail)

            pickle.dump(phone, output_file)

            again = input('Введёте ещё один элемент данных? (д/н)')

    print('Данные записаны в', FILENAME)


main()
