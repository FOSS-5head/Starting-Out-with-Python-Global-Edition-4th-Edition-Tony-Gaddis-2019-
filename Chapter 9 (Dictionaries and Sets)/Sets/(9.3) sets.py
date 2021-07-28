# Эта программа демонстрирует различные операции над множествами.
baseball = set(['Джоди', 'Кармен', 'Аида', 'Алиция'])
basketball = set(['Эва', 'Кармен', 'Алиция', 'Сара'])

# Показать членов бейсбольного множества.
print('Эти студенты состоят в бейсбольной команде: ')
for name in baseball:
    print(name)

# Показать членов баскетбольного множества.
print()
print('Эти студенты состоят в баскетбольной команде:')
for name in basketball:
    print(name)

# Продемонстрировать пересечение.
print()
print('Эти студенты играют и в бейсбол, и в баскетбол:')
for name in baseball.intersection(basketball):
    print(name)

# Продемонстрировать объединение.
print()
print('Эти студенты играют в одну или обе спортивные игры:')
for name in baseball.union(basketball):
    print(name)

# Продемонстрировать разность между бейсболом и баскетболом.
print()
print('Эти студенты играют в бейсбол, но не в баскетбол:')
for name in baseball.difference(basketball):
    print(name)

# Продемонстрировать разность между баскетболом и бейсболом.
print()
print('Эти студенты играют в баскетбол, но не в бейсбол:')
for name in basketball.difference(baseball):
    print(name)

# Продемонстрировать симметрическую разность.
print()
print('Эти студенты играют в одну из спортивных игр, но не в обе:')
for name in baseball.symmetric_difference(basketball):
    print(name)
