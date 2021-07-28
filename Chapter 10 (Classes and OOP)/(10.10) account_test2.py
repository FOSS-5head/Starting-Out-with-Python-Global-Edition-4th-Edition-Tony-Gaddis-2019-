from modules import bankaccount2


def main():
    start_bal = float(input('Введите свой начальный остаток: '))

    savings = bankaccount2.BankAccount(start_bal)
    pay = float(input('Сколько Вы получили на этой неделе? '))
    # savings
    print('Вношу эту сумму на Ваш счет.')
    savings.deposit(pay)
    print(savings)
    # cash
    cash = float(input('Какую сумму Вы желаете снять со счета? '))
    print('Снимаю эту сумму с Вашего банковского счета.')
    savings.withdraw(cash)

    print(savings)


main()
