def main():
    the_audience, teachers, time = config()
    menu()
    num_course = input('Введите номер курса: ')
    print('Время:', time.get(num_course, 'Не назначено.'))
    print('Учитель:', teachers.get(num_course, 'Не назначено.'))
    print('Аудитория №:', the_audience.get(num_course, 'Не назначено.'))


def menu():
    print()
    print('Введите один из курсов, показанных ниже',
          'и получите полную информацию.\n')
    print('CS101, CS102, CS103, NT110, CM241, CS104, CS105')
    print()


def config():

    the_audience = {'CS101': 3004,
                    'CS102': 4501,
                    'CS103': 6755,
                    'CS104': 1244,
                    'CS105': 1411}

    teachers = {'CS101': 'Хайнс',
                'CS102': 'Альварадо',
                'CS103': 'Рич',
                'NT110': 'Берк',
                'CM241': 'Ли'}

    time = {'CS101': '8:00',
            'CS102': '9:00',
            'CS103': '10:00',
            'NT110': '11:00',
            'CM241': '13:00'}

    return the_audience, teachers, time


main()
