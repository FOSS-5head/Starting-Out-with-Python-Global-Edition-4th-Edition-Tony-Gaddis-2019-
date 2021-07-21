assessed_value = 60
tax = 0.72


def main():
    cost = float(input('Введите фактическую стоимость недвижимости: '))
    assessed_value1 = (cost / 100) * assessed_value
    tax2 = cost * 0.72
    print('Налог составляет:', format(tax2, '.2f'),
          '\nоценочная стоимость:', format(assessed_value1, '.2f'))


main()
