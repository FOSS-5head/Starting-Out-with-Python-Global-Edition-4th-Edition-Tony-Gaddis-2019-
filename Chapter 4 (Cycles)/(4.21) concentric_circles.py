# Концентрические круги. 
import turtle 
 
# Именованные константы(переменных). 
NUМ_CIRCLES=20 
STARTING_RADIUS = 20
OFFSET = 10
ANIМATION_SPEED = 0

# Настроить черепаху. 
turtle.speed(ANIМATION_SPEED) 
turtle.hideturtle()

# Задать радиус первого круга. 
radius = STARTING_RADIUS 

#Нарисовать круги. 
for count in range(NUМ_CIRCLES):
    # Нарисовать круг.
    turtle.circle(radius)
 
    # Получить координаты следующего круга. 
    x = turtle.xcor() 
    у = turtle.ycor() - OFFSET 

    # Вычислить радиус следующего круга. 
    radius += OFFSET 

    # Позиция черепахи для следующего круга. 
    turtle.penup() 
    turtle.goto(x, у) 
    turtle.pendown()
    