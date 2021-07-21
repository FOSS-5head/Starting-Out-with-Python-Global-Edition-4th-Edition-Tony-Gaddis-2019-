countries = {'Украина': 'Киев',
             'Россия': 'Москва',
             'Германия': 'Берлин',
             'Испания': 'Мадрид',
             'Беларусь': 'Минск'}

wrong_answers = 0
correct_answers = 0

print('Как вас зовут?')
name = input()
print('Привет,', name + '! Твой первый вопрос!')

again = 'д'
while again == 'д' or again == 'Д':
    for key in countries:
        print(key)
        answer = input('Какая столица этой страны?: ')
        if answer in countries[key]:
            correct_answers += 1
            print('Правильно! Двигаемся дальше!\n')

        elif answer not in countries[key]:
            wrong_answers += 1
            print('Неправильно :(\n')

    print('Итого у вас:')
    print('Правильных ответов:', correct_answers)
    print('Неправильных ответов:', wrong_answers)
    print('\nПовторить викторину,', name + '? (д/н): ')
    again = input()

    wrong_answers = 0
    correct_answers = 0
