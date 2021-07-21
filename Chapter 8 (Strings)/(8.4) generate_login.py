# -*- coding: cp1251 -*-

from login import get_login_name as login


def main():
    first = input('Введите свое имя: ')
    last = input('Введите свою фамилию: ')
    idnumber = input('Введите свой номер студента: ')

    print('Ваше имя для входа в систему:')
    print(login(first, last, idnumber))


main()
