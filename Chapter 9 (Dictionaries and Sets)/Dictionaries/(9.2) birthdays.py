# Эта программа применяет словарь для хранения
# имен и дней рождения друзей.

# Глобальные константы для пунктов меню
LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
DEMONSTRATION = 5
CLEAR = 6
QUIT = 7


# Главная функция.
def main():
    # Создать пустой словарь.
    birthdays = {}

    # Инициализировать переменную для выбора пользователя.
    choice = 0

    while choice != QUIT:
        # Получить выбранный пользователем пункт меню.
        choice = get_menu_choice()

        # Обработать выбранный вариант действий.
        if choice == LOOK_UP:
            look_up(birthdays)
        elif choice == ADD:
            add(birthdays)
        elif choice == CHANGE:
            change(birthdays)
        elif choice == DEMONSTRATION:
            demonstration(birthdays)
        elif choice == CLEAR:
            clear(birthdays)
        elif choice == DELETE:
            delete(birthdays)


def get_menu_choice():
    print()
    print('Друзья и их дни рождения')
    print('-------------------------')
    print('1. Найти день рождения')
    print('2. Добавить новый день рождения')
    print('3. Изменить день рождения')
    print('4. Удалить день рождения')
    print('5. Показать записанные данные пользователем')
    print('6. Очистить записанные данные.')
    print('7. Выйти из программы')
    print()

    try:
        choice = int(input('Введите выбранный пункт: '))
        while choice < LOOK_UP or choice > QUIT:
            choice = int(input('Введите выбранный пункт: '))
        return choice

    except ValueError:
        print('Введены неправильные данные, попробуйте ещё раз.')


def look_up(birthdays):
    name = input('Введите имя: ')

    print(birthdays.get(name, 'Не найдено.'))


def add(birthdays):
    name = input('Введите имя: ')
    bday = input('Введите день рождения: ')

    if name not in birthdays:
        birthdays[name] = bday

    else:
        print('Эта запись уже сущевствует.')


def change(birthdays):
    name = input('Введите имя')

    if name in birthdays:
        bday = input('Введите новый день рождения: ')

        birthdays[name] = bday
    else:
        print('Это имя не найдено')


def demonstration(birthday):
    print('Введеный список составляет:')
    for i in birthday:
        print(i, '(' + birthday[i] + ')')


def clear(birthday):
    print('Был список:')
    for i in birthday:
        print(i, '(' + birthday[i] + ')')

    birthday.clear()
    print('\nСписок успешно очищен!')


def delete(birthdays):
    name = input('Введите имя: ')

    if name in birthdays:
        del birthdays[name]
    else:
        print('Это имя не найдено.')


main()
