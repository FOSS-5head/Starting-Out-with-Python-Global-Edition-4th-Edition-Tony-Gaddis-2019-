class BankAccount:
    def __init__(self, bal):
        self.__balance = bal

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount

        else:
            print('Ошибка: недостаточно средств')

    def __str__(self):
        return 'Остаток составляет $' + format(self.__balance, '.2f')
