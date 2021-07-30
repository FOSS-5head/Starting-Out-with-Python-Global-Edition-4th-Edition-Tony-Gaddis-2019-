from modules import vehicles


def main():
    # Создать объект на основе класса Car.
    # Легковое авто: 2007 Audi с 12500 миль пробега,
    # ценой $21500.00 и с 4 дверьми.
    used_car = vehicles.Car('Audi', 2007, 12500, 21500.0, 4)

    # Показать данные легкового авто.
    print(f'Изготовитель: {used_car.get_make()}')
    print(f'Модель: {used_car.get_model()}')
    print(f'Пробег {used_car.get_mileage()}')
    print(f'Цена: {used_car.get_price()}')
    print(f'Кол-во дверей: {used_car.get_doors()}')


main()
