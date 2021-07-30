# Класс SavingsAccount представляет
# сберегательный счет.


class SavingsAccount:
    # Метод init принимает аргументы для
    # номера счета, процентной ставки и остатка.
    def __init__(self, account_num, int_rate, bal):
        self.__account_num = account_num
        self.__interest_rate = int_rate
        self.__balance = bal

    def set_account_num(self, account_num):
        self.__account_num = account_num

    def set_interest_rate(self, int_rate):
        self.__interest_rate = int_rate

    def set_balance(self, bal):
        self.__balance = bal

    def get_account_num(self):
        return self.__account_num

    def get_interest_rate(self):
        return self.__interest_rate

    def get_balance(self):
        return self.__balance


# К.пасс СО представляет счет
# депозитного сертификата (СО) .
# Это подкласс класса SavingsAccount.
class CD(SavingsAccount):
    # Метод init принимает аргументы для
    # номера счета, процентной ставки, остатка
    # и даты погашения.
    def __init__(self, account_num, int_rate, bal, mat_date):
        SavingsAccount.__init__(self, account_num, int_rate, bal)

        self.__maturity_date = mat_date

    # Метод set_maturity_date является методом-модификатором
    # атрибута _maturity_date.

    def set_maturity_date(self, mat_date):
        self.__maturity_date = mat_date

    def get_maturity_date(self):
        return self.__maturity_date
