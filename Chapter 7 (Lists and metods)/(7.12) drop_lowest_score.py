# Эта программа получает серию оценок за лабораторные
# работы и вычисляет среднюю оценку,
# отбрасывая самую низкую.


def main():
    try:
        # Получить от пользователя оценки.
        scores = get_scores()

        # Получить сумму оценок.
        total = get_total(scores)

        # Получить самую низкую оценку.
        lowest = min(scores)

        # Вычесть самую низкую оценку из суммы.
        total -= lowest

        # Вычислить среднее значение. Обратите внимание, что
        # мы делим на количество оценок минус 1, потому что
        # самая низкая оценка была отброшена.
        average = total / (len(scores) - 1)

        # Показать среднее значение.
        print('Средняя оценка с учетом отброшенной',
              'самой низкой оценкой составляет:', average)

    except ZeroDivisionError:
        print('Произошла ошибка ZeroDivisionError, пожалуйста, попробуйте ещё раз.')
    except ValueError:
        print('Произошла ошибка ValueError, пожалуйста, попробуйте вводить числовые данные.')


def get_scores():
    test_scores = []
    again = 'д'

    while again == 'д':
        value = float(input('Введите оценку: '))
        test_scores.append(value)

        print('Желаете добавить ещё одну оценку?')
        again = input('д = да, все остальное = нет: ')
        print()

    return test_scores


def get_total(value_list):
    total = 0.0

    for num in value_list:
        total += num

    return total


main()
