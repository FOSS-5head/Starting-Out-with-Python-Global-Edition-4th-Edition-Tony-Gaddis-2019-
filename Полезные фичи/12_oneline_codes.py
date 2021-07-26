# Информация взята с видео: https://www.youtube.com/watch?v=LkHCy5JZtsA
# 12 полезных фич на Python
from functools import reduce


# Записывает данные в 3 переменные через пробел
# (Как строки):
def input_strings():
    x, y, z = input('Введите значения: ').strip().split()
    print(f'{x=}, {y=}, {z=}')


# Записывает данные в 3 переменные через пробел
# (Как целочисленные):
def input_int():
    x, y, z = input('Введите числовые значения: ').strip().split()
    x, y, z = map(int, (x, y, z))
    print(f'{x=}, {y=}, {z=}')
    print(x*y*z)


# Записывает данные в 3 переменные через пробел,
# а после этого эти данные можно разом задействовать с помощью функции reduce():
def input_reduce():
    volume = reduce(lambda x, y: x * y,
                    map(int, input().strip().split()))
    print(f"{volume = }")


# Фильтрация через цикл for:
def comprehensions():
    names = ['Христофор', 'Адемар', 'Тэя', 'Стэфания', 'Архип']
    names_starts_a = [name for name in names if name.startswith('А')]
    print(names_starts_a)


# Фильтрация по первому знаку в списке через фукнцию filter():
def filter1():
    names = ['Христофор', 'Адемар', 'Тэя', 'Стэфания', 'Архип']
    names_starts_a = filter(lambda name: name.startswith('А'), names)
    print(tuple(names_starts_a))


# Копирование данных в другой список путем среза:
def copy_list():
    num = [1, 2, 3]
    num1 = num[:]
    print(f'{num1 = }, {num = }')


# Проверяет, есть ли в переменной name заданные строки:
def check_name():
    name = "Петр"
    if name in ('Алексей', "Петр", 'Христофор'):
        print(name)


# Проверяет на истинность все переменные при помощи all():
def all_true():
    a = b = c = d = e = True
    # Можно было бы проверить все значения на True путем and:
    '''
    if a and b and c and d and e:
        print("All True")
    '''
    # Но легче сделать вот так:
    if all((a, b, c, d, e)):
        print('All True')


# Проверяет на истинность любую переменную при помощи any():
def any_true():
    a = b = c = d = e = True
    # Можно было бы проверить все значения на True путем or:
    '''
    if a or b or c or d or e:
        print("All True")
    '''
    # Но легче сделать вот так:
    if any((a, b, c, d, e)):
        print('All True')
