def main():
    cost = float(input('Введите стоимость имущества: $'))
    total = (cost / 100) * 80
    print('Стоимость имущества: $', format(cost, '.2f'),
          '\nСтоимость страховки: $', format(total, '.2f'), sep='')


main()
