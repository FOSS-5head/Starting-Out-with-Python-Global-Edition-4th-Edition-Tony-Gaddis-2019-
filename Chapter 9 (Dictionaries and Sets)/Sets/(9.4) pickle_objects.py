import pickle


def main():
    again = 'д'
    output_file = open('(9.4) info.dat', 'wb')

    while again.lower() == 'д':
        save_data(output_file)

        again = input('Желаете ввести ещё данные? (д/н)')

    output_file.close()


def save_data(file):
    person = {'Имя': input('Имя: '),
              'Возраст': int(input('Возраст: ')),
              'Масса': float(input('Масса: '))}

    pickle.dump(person, file)


main()
