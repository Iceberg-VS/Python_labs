import math

# Исходный словарь с координатами городов
sites = {
    'Moscow': (550,  370),
    'London': (510,  510),
    'Paris': (480,  480),
}

# Функция для вычисления расстояния между двумя точками
def distance(coord1, coord2):
    x1, y1 = coord1
    x2, y2 = coord2
    return math.sqrt((x1 - x2) **  2 + (y1 - y2) **  2)

# Создаем словарь для хранения расстояний между городами
distances = {}

# Перебираем все пары городов
for city1, coord1 in sites.items():
    for city2, coord2 in sites.items():
        if city1 != city2:  # чтобы не считать расстояние города до самого себя
            # Вычисляем расстояние и добавляем его в словарь
            distances[(city1, city2)] = distance(coord1, coord2)

# Выводим словарь расстояний
print("\n",distances)
