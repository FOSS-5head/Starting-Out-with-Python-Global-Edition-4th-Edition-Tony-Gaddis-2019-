# Программа демонстрирует замыкание.


# Пример НЕ замыкания.
def not_adder(n, m):
    return n + m


# Пример переделанного кода выше на замыкание.
def adder(n):
    def fn(m):
        return n + m
    return fn


# Тоже самое можно выразить с помощью lambda функций.
def lambda_adder():
    adder1 = lambda n: lambda m: n+m
    print(adder1)
