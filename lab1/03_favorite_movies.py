# Есть значение радиуса круга
radius = 42

# Выведите на консоль значение прощади этого круга с точностю до 4-х знаков после запятой
# подсказки:
#       формулу можно подсмотреть в интернете,
#       пи возьмите равным 3.1415926
#       точность указывается в функции round()
# TODO здесь ваш код
P = 3.1415
a = 42
S = P * a * a
print(round(S, 4))

# Далее, пусть есть координаты точки
point_1 = (23, 34)
# где 23 - координата х, 34 - координата у

# Если точка point лежит внутри того самого круга [центр в начале координат (0, 0), radius = 42],
# то выведите на консоль True, Или False, если точка лежит вовне круга.
# подсказки:
#       нужно определить расстояние от этой точки до начала координат (0, 0)
#       формула так же есть в интернете
#       квадратный корень - это возведение в степень 0.5
#       операции сравнения дают булевы константы True и False
# TODO здесь ваш код
point_1 = (23, 34)
x, y = point_1
centr = (0, 0)
centr_x, centr_y = centr
radius = 42
distance = 0.5 * (((x - centr_x) ** 2) + ((y - centr_y) ** 2))
inside_circle = distance <= radius
print(inside_circle)

point_2 = (30, 30)
# Если точка point_2 лежит внутри круга (radius = 42), то выведите на консоль True,
# Или False, если точка лежит вовне круга.
# TODO здесь ваш код

point_1 = (30, 30)
x, y = point_1
centr = (0, 0)
centr_x, centr_y = centr
radius = 42
distance = 0.5 * (((x - centr_x) ** 2) + ((y - centr_y) ** 2))
inside_circle = radius <= distance
print(inside_circle)