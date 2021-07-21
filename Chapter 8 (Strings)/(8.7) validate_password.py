import login2


def main():
    password = input('Введите свой пароль: ')

    while not login2.valid_password(password):
        print('Этот пароль недопустим.')
        password = input('Введите свой пароль: ')

    print('Это допустимый пароль.')


main()
