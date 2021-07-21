# Эта программа показывает записи, которые
# находятся в файле (6.13) employees.txt.


def main():
    emp_file = open('(6.13) employees.txt', 'r')
    name = emp_file.readline()

    while name != '':
        id_num = emp_file.readline()
        dept = emp_file.readline()

        name = name.rstrip('\n')
        id_num = id_num.rstrip('\n')
        dept = dept.rstrip('\n')

        print('Имя:', name)
        print('ИД:', id_num)
        print('Отдел:', dept)
        print()

        name = emp_file.readline()

    emp_file.close()


main()
