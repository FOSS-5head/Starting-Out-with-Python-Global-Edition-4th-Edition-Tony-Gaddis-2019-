# Эта программа создает экземпляр класса SavingsAccount
# и экземпляр класса CD.

from modules import accounts


def main():
    # Получить номер счета, процентную ставку,
    # и остаток сберегательного счета.
    print('Введите данные о сберегательном счете.')
    acct_num = input('Номер счета: ')
    int_rate = float(input('Остаток: '))
    balance = float(input('Остаток: '))

    savings = accounts.SavingsAccount(acct_num, int_rate, balance)

    # Получить номер счета, процентную ставку,
    # остаток счета и дату погашения счета СО.
    print('Введите данные о счете CD.')
    acct_num = input('Номер счета: ')
    int_rate = float(input('Процентная ставка: '))
    balance = float(input('Остаток: '))
    maturity = input('Дата погашения: ')

    # Создать объект CD.
    cd = accounts.CD(acct_num, int_rate, balance, maturity)

    # Показать введеные данные.
    print('Вот введенные Вами данные:\n')
    print('Сберегательный счет')
    print('-------------------')
    print(f'Номер счета: {savings.get_account_num()}'
          f'\nПроцентная ставка: {savings.get_interest_rate()}'
          f'\nОстаток: $', format(savings.get_balance(), '.2f'), sep='')
    print(f'\n\nСчет депозитного сертификата: (CD)')
    print('---------------------------------')
    print(f'Номер счета: {cd.get_account_num()}'
          f'\nПроцентная ставка: {cd.get_interest_rate()}'
          f'\nОстаток: $', format(cd.get_balance(), '.2f'), sep='')
    print(f'Дата погашения:{cd.get_maturity_date()}')


main()
