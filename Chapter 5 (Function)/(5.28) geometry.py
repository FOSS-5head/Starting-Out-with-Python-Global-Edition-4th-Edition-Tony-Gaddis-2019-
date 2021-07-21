# Эта программа позволяет пользователю выбирать различные
# геометрические вычисления из меню.
# Программа импортирует модули circle и rectangle.

import circle
import rectangle

# Константы для элементов меню.
AREA_CIRCLE_CHOICE = 1
CIRCUMFERENCE_CHOICE = 2
AREA_RECTANGLE_CHOICE = 3
PERIMETER_RECTANGLE_CHOICE = 4
QUIT_CHOICE = 5


# Главная функция.
def main():
    choice = 0

    while choice != QUIT_CHOICE:
        display_menu()

        choice = int(input('Выберите вариант: '))

        if choice == AREA_CIRCLE_CHOICE:
            radius = float(input('Введите радиус круга: '))
            print("Площадь равна", circle.area(radius))
        elif choice == CIRCUMFERENCE_CHOICE:
            radius = float(input('Введите радиус круга: '))
            print('Длина окружности равна',
                  circle.circumference(radius))
        elif choice == AREA_RECTANGLE_CHOICE:
            width = float(input('Введите ширину прямоугольника: '))
            length = float(input('Введите длину прямогульника:'))
            print('Площадь равна', rectangle.area(width, length))
        elif choice == PERIMETER_RECTANGLE_CHOICE:
            width = float(input('Введите ширину прямоугольника: '))
            length = float(input('Введите длина прямоугольника: '))
            print('Периметр равен',
                  rectangle.perimeter(width, length))
        elif choice == QUIT_CHOICE:
            print('Выходим из программы...')
        else:
            print('Ошибка: недопустимый выбор.')


def display_menu():
    print('----------------------------')
    print('МЕНЮ')
    print('1. Площадь круга')
    print('2. Длина окружности')
    print('3. Площадь прямоугольника')
    print('4. Периметр прямоугольника')
    print('5. Выход')
    print('----------------------------')


main()
