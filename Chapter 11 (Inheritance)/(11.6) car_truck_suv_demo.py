# Эта программа создает объекты Car, Truck
# и SUV.
from modules import vehicles


def main():
    # Создать объект Car для подержанного авто 2001 вмw
    # с 70000 милями пробега, ценой $15000,
    # с 4 дверьми.
    car = vehicles.Car('BMW', 2001, 70000, 15000.0, 4)

    # Создать объект Truck для подержанного пикапа 2002
    # Toyota с 40000 милями пробега, ценой
    # $12000 и с 4-колесным приводом.
    truck = vehicles.Truck('Toyota', 2002, 40000, 12000.0, '4WD')

    # Создать объект SUV для подержанного 2000
    # Volvo с 30000 милями пробега, ценой
    # $18500 и вместимостью 5 человек.
    suv = vehicles.SUV('Volvo', 2000, 30000, 18500.0, 5)

    print('ПОДЕРЖАННЫЕ АВТО НА СКЛАДЕ')
    print('==========================')

    # (?) подробнее про f'' строки можете посмотреть здесь (29-50 строки кода):
    # https://shultais.education/blog/python-f-strings

    # Показать данные легкового авто.
    print(f'\nДанный легковой автомобиль имеется на складе:'
          f'\nИзготовитель: {car.get_make()}'
          f'\nМодель: {car.get_model()}'
          f'\nПробег: {car.get_mileage()}'
          f'\nЦена: {car.get_price()}'
          f'\nКол-во дверей: {car.get_doors()}')

    # Показать данные пикапа.
    print(f'\nДанный пикап имеется на складе:'
          f'\nИзготовитель: {truck.get_make()}'
          f'\nМодель: {truck.get_model()}'
          f'\nПробег: {truck.get_mileage()}'
          f'\nЦена: {truck.get_price()}'
          f'\nТип привода: {truck.get_drive_type()}')

    # Показать данные джипа.
    print(f'\nДанный джип имеется на складе:'
          f'\nИзготовитель: {suv.get_make()}'
          f'\nМодель: {suv.get_model()}'
          f'\nПробег: {suv.get_mileage()}'
          f'\nЦена: {suv.get_price()}'
          f'\nПассажирская вместимость: {suv.get_pass_cap()}')


main()
