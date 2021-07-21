a = input('Введите ключ: ')
b = input('Введите значение ключа: ')
dct = {a: b}
if 'Джим' in dct:
    dct.pop(a)
    print(dct)
else:
    print('Значения Джим в словаре не сущетсвует!')
