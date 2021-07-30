# Класс Mammal представляет род млекопитающих.
class Mammal:

    # Метод init принимает аргумент для
    # вида млекопитающего.
    def __init__(self, species):
        self._species = species

    # Метод show_species выводит сообщение
    # о виде млекопитающего.
    def show_species(self):
        print('Я -', self._species)

    # Метод make_sound издает характерный
    # для всех млекопитающих звук.
    def make_sound(self):
        print('Грррррр')


# Класс Dog является подклассом класса Mammal.
class Dog(Mammal):
    def __init__(self):
        Mammal.__init__(self, 'собака')

    def make_sound(self):
        print('Гав-гав')


class Cat(Mammal):
    def __init__(self):
        Mammal.__init__(self, 'кот')

    def make_sound(self):
        print('Мяу!')
