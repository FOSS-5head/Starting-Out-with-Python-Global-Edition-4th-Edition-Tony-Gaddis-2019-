set1 = set((input('Введите множество 1: ').split()))
set2 = set(input('Введите множество 2: ').split())


def set_with_for():
    for i in set1.intersection(set2):
        print(i)
    print('-------------')


def set_with_module():
    set3 = set1.intersection(set2)
    print(set3)
    print()


set_with_module()
