# Эта программа вычисляет выплату продавцу
# в компании 'Делай свою музыку'.


def main():
    # Получить сумму продаж.
    sales = get_sales()

    # Получить сумму авансовой оплаты.
    advanced_pay = get_advanced_pay()

    # Определить ставку комиссионных.
    comm_rate = determine_comm_rate(sales)

    # Рассчитать оплату.
    pay = sales * comm_rate - advanced_pay

    # Показать сумму вьплаты.
    print('Выплата составляет $', format(pay, '.2f'), sep='')

    # Определить, является ли выплата отрицательной.
    if pay < 0:
        print('Продавец должен возместить разницу')
        print('компании.')


def get_sales():
    monthly_sales = float(input('Введите сумму месячных продаж: '))
    return monthly_sales


def get_advanced_pay():
    print('Введите сумму авансовой выплаты либо')
    print('введите 0, если такой выплаты не было.')
    advanced = float(input('Авансовая выплата: '))

    return advanced


def determine_comm_rate(sales):
    if sales < 10000.00:
        rate = 0.10
    elif 10000 <= sales <= 14999.99:
        rate = 0.12
    elif 15000 <= sales <= 17999.99:
        rate = 0.14
    elif 18000 <= sales <= 21999.99:
        rate = 0.16
    else:
        rate = 0.18

    return rate


main()
