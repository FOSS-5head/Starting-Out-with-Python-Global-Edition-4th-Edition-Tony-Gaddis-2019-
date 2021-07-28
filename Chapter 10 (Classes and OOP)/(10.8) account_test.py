from modules import bankaccount


def main():
    start_bal = float(input('Введите свой начальный остаток: '))
    savings = bankaccount.BankAccount(start_bal)

    pay = float(input('Сколько Вы получили на этой неделе? '))
    print('Вношу эту сумму на Ваш счёт.')
    savings.deposit(pay)

    print('Ваш остаток на банковском счете составляет $',
          format(savings.get_balance(), '.2f'),
          sep='')
    cash = float(input('Какую сумму Вы желаете снять со счета? '))
    print('Снимаю эту сумму с Вашенго банковского счета.')
    savings.withdraw(cash)

    print('Ваш остаток на банковском счете составляет $',
          format(savings.get_balance(), '.2f'),
          sep='')


main()
