# LEGENDARY COMPLEXITY (130 lines)
import random


def main():
    name1, name2 = welcome()
    deck = create_deck()
    deck = change_deck(deck)
    deck = shuffle(deck)
    deal_cards(deck, name1, name2)


def welcome():
    print('Приветствую, это мини игра в блек-джек!\n'
          'Для начала, введите имя первого пользователя:')
    first_name = input()
    print('А теперь, введите имя второго пользователя:')
    second_name = input()

    return first_name, second_name


def create_deck():
    deck = {'Туз пик': 1, '2 пик': 2, '3 пик': 3,
            '4 пик': 4, '5 пик': 5, '6 пик': 6,
            '7 пик': 7, '8 пик': 8, '9 пик': 9,
            '1О пик': 10, 'Валет пик': 10,
            'Дама пик': 10, 'Король пик': 10,

            'Туз червей': 1, '2 червей': 2, '3 червей': 3,
            '4 червей': 4, '5 червей': 5, '6 червей': 6,
            '7 червей': 7, '8 червей': 8, '9 червей': 9,
            '1О червей': 10, 'Валет червей': 10,
            'Дама червей': 10, 'Король червей': 10,

            'Туз треф': 1, '2 треф': 2, '3 треф': 3,
            '4 треф': 4, '5 треф': 5, '6 треф': 6,
            '7 треф': 7, '8 треф': 8, '9 треф': 9,
            '1О треф': 10, 'Валет треф': 10,
            'Дама треф': 10, 'Король треф': 10,

            'Туз бубей': 1, '2 бубей': 2, '3 бубей': 3,
            '4 бубей': 4, '5 бубей': 5, '6 бубей': 6,
            '7 бубей': 7, '8 бубей': 8, '9 бубей': 9,
            '1О бубей': 10, 'Валет бубей': 10,
            'Дама бубей': 10, 'Король бубей': 10}

    return deck


def shuffle(deck):
    l1 = list(deck.items())
    random.shuffle(l1)
    deck = dict(l1)

    return deck


def change_deck(deck):
    change = int(input('Введите значение 1 или 11 для тузов: '))

    while change > 11 or change < 1:
        change = int(input('Введите значение 1 или 11 для тузов ещё раз: '))

    deck['Туз пик'] = change
    deck['Туз червей'] = change
    deck['Туз треф'] = change
    deck['Туз бубей'] = change

    return deck


def deal_cards(deck, first_name, second_name):
    list1 = []
    list2 = []

    hand_value1 = 0
    hand_value2 = 0

    while True:
        if hand_value1 > 21 and hand_value2 > 21:
            print('\nНикто не выиграл!')
            print('\nИтого у вас:')
            print('У пользователя', first_name, hand_value1, 'очков')
            print('А у пользователя', second_name, hand_value2, 'очков\n')

            print('Карты на руках у ', first_name, ':', sep='')
            print(', '.join(tuple(list1)))
            print()
            print('\nКарты на руках у ', second_name, ':', sep='')
            print(', '.join(tuple(list2)))

            break

        elif hand_value1 > 21:
            print('\nПользователь', second_name, 'Выиграл, поздравляю с победой!')
            print('\nИтого у вас:')
            print('У пользователя', first_name, hand_value1, 'очков')
            print('А у пользователя', second_name, hand_value2, 'очков\n')

            print('Карты на руках у ', first_name, ':', sep='')
            print(', '.join(tuple(list1)))
            print()
            print('Карты на руках у ', second_name, ':', sep='')
            print(', '.join(tuple(list2)))
            break

        elif hand_value2 > 21:
            print('\nПользователь', first_name, 'Выиграл, поздравляю с победой!')
            print('\nИтого у вас:')
            print('У пользователя', first_name, hand_value1, 'очков')
            print('А у пользователя', second_name, hand_value2, 'очков\n')

            print('Карты на руках у ', first_name, ':', sep='')
            print(', '.join(tuple(list1)))
            print()
            print('Карты на руках у ', second_name, ':', sep='')
            print(', '.join(tuple(list2)))
            break

        card1, value1 = deck.popitem()
        card2, value2 = deck.popitem()

        list1.append(card1)
        list2.append(card2)

        hand_value1 += value1
        hand_value2 += value2


main()
