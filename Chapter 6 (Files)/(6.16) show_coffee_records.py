def main():
    coffee_file = open('(6.15)coffee.txt', 'r')
    descr = coffee_file.readline()
    while descr != '':
        qty = float(coffee_file.readline())

        descr = descr.rstrip('\n')

        print('Описание:', descr)
        print('Количество:', qty)
        descr = coffee_file.readline()

    coffee_file.close()
    

main()
