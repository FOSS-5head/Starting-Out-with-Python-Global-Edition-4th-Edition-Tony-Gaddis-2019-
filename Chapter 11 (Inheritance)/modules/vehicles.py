# Класс Automobile содержит общие данные
# об автомобиле на складе.
class Automobile:

    # Метод init_method принимает аргументы для
    # фирмы-изготовителя, модели, пробега и цены.
    # Он инициализирует атрибуты данных этими значениями.

    def __init__(self, make, model, mileage, price):
        self.__make = make
        self.__model = model
        self.__mileage = mileage
        self.__price = price

    # Следуюшие ниже методы являються методами-модификаторами
    # атрбитуов данных этого класса.

    def set_make(self, make):
        self.__make = make

    def set_model(self, model):
        self.__model = model

    def set_mileage(self, mileage):
        self.__mileage = mileage

    def set_price(self, price):
        self.__price = price

    # Следующие ниже методы являются методами-получателями
    # атрибутов данных этого класса.

    def get_make(self):
        return self.__make

    def get_model(self):
        return self.__model

    def get_mileage(self):
        return self.__mileage

    def get_price(self):
        return self.__price


# Класс Car представляет легковой автомобиль.
# Он является подклассом класса AutomoЬile.
class Car(Automobile):
    def __init__(self, make, model, mileage, price, doors):
        Automobile.__init__(self, make, model, mileage, price)

        self.__doors = doors

    def set_doors(self, doors):
        self.__doors = doors

    def get_doors(self):
        return self.__doors


# Класс Truck представляет пикап.
# Он является подклассом класса Automobile.
class Truck(Automobile):
    def __init__(self, make, model, mileage, price, drive_type):
        Automobile.__init__(self, make, model, mileage, price)

        self.__drive_type = drive_type

    def set_drive_type(self, drive_type):
        self.__drive = drive_type

    def get_drive_type(self):
        return self.__drive_type


# Класс SUV представляет джип.
# Он является подклассом класса Automobile.
class SUV(Automobile):
    def __init__(self, make, model, mileage, price, pass_cap):
        Automobile.__init__(self, make, model, mileage, price)

        self.__pass_cap = pass_cap

    def set_pass_cap(self, pass_cap):
        self.__pass_cap = pass_cap

    def get_pass_cap(self):
        return self.__pass_cap
