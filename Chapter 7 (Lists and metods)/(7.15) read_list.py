# ��� ��������� ��������� ���������� ����� � ������.


def main():
    # ������� ���� ��� ������.
    infile = open('(7.14) cities.txt', 'r')

    # ��������� ���������� ����� � ������.
    cities = infile.readlines()

    # ������� ����.
    infile.close()

    # ������� �� ������� �������� ������ \n.
    index = 0
    while index < len(cities):
        cities[index] = cities[index] .rstrip('\n')
        index += 1

    # ���������� ���������� ������.
    print(cities)


# ������� ������� �������.
main()
