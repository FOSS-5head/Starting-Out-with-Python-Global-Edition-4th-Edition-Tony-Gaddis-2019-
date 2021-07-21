another = "back"
while another == 'back':
    print()
    login = str(input('Введите свой ник: '))
    password = str(input('Введите пароль: '))
    re_password = str(input('Введите свой пароль ещё раз: '))
    if re_password != password:
        print()
        print('Вы ввели не правильный пароль, введите \'back\' что бы повторить операцию.')
        another = input('(Введите слово "back", что бы вернутся назад): ')
    
    elif re_password == password:
        print()
        print('Вы успешно зарегистрировались под логином \"'+login+'\"')
        another = input('(Введите слово "back", что бы вернутся назад): ')
