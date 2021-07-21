# Эта программа выводит прямоугольную комбинацию 
# звездочек. 
rows = int(input('Cкoлькo строк? '))
cols = int(input('Cкoлькo столбцов? '))

for r in range(rows):
    for i in range(cols):
        print('*', end=' ')
    print()
