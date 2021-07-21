# Переменные

Base_hours = 40  # Базовые часы в неделю
Multiplier = 1.5  # Мультипликатор сверхурочного времени

hours = float(input('Сколько часов вы проработали: '))
pay_rate = float(input('Введите почасовую ставку оплаты труда: '))

# Рассчитуем и показываем заработную плату до удержаний.
if hours > Base_hours:
    overtime_hours = hours - Base_hours

    overtime_pay = overtime_hours * pay_rate * Multiplier
    
    gross_pay = Base_hours * pay_rate + overtime_pay

else:
    gross_pay = hours * pay_rate

print('Заработная плата до удержаний составляет: $',
    format(gross_pay, ',.2f'), sep='')
