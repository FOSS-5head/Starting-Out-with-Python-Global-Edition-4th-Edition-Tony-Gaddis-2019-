# -*- coding: cp1251 -*-

from login import get_login_name as login


def main():
    first = input('������� ���� ���: ')
    last = input('������� ���� �������: ')
    idnumber = input('������� ���� ����� ��������: ')

    print('���� ��� ��� ����� � �������:')
    print(login(first, last, idnumber))


main()
