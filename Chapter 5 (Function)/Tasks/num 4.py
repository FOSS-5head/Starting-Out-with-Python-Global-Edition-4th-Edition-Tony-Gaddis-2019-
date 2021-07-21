year_cost = 365
month_cost = 30


def main():
    print('-----------------------------------')
    sum = sum1()
    print('-----------------------------------')
    print('Сумма всего выходит:', format(sum, '.2f'))
    month = month_cost * sum
    print('Месячная сумма:', month)
    year = year_cost * sum
    print('Ежегодная сумма выходит:', year)
    print('-----------------------------------')


def sum1():
    credit = float(input('Введите стоимость кредита: '))
    insurance = float(input('Введите стоимость страховка: '))
    petrol = float(input('Введите стоимость бензин: '))
    machine_oil = float(input('Введите стоимость машинное масло: '))
    tires = float(input('Введите стоимость шины: '))
    maintenance = float(input('Введите стоимость техосблуживания: '))
    sum2 = credit + insurance + petrol + machine_oil + tires + maintenance
    return sum2


main()
