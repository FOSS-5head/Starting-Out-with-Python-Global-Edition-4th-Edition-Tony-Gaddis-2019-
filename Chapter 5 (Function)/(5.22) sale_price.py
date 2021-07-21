# Эта программа вычисляет отпускную цену
# розничого товара.

# DISCOUNT_PERCENTAGE используется в качестве
# глобальной константы для процента скидки.
DISCOUNT_PERCENTAGE = 0.20


# Главная функция.
def main():
    # Получить обычную цену товара.
    reg_price = get_regular_price()

    # Рассчитать отпускную цену.
    sale_price = reg_price - discount(reg_price)

    # Показать отпускную цену.
    print('Отпускная цена составляет$',
          format(sale_price, '.2f'), sep=' ')


# Функция get_regular_price предлагает пользователю
# ввести обычную цену товара и возвращает
# это значение.
def get_regular_price():
    price = float(input("Bвeдитe обычную цену товара: "))
    return price


# Функция discount принимает цену товара в качестве
# аргумента и возвращает сумму скидки,
# указанную в DISCOUNT_PERCENTAGE.
def discount(price):
    return price * DISCOUNT_PERCENTAGE


# Вызвать главную функцию.
main()
