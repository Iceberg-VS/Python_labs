#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Есть словарь координат городов

sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}

# Составим словарь словарей расстояний между ними
# расстояние на координатной сетке - ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

def calculations(city1,city2,sites):
    result=0.0
    x1, y1 = sites[city1]
    x2, y2 = sites[city2]
    result=(((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5)
    return round(result)

distances = {}
for city1 in sites:
    distances[city1] = {}
    for city2 in sites:
        if (city1 != city2):
            S = calculations(city1, city2, sites)
            distances[city1][city2] = S
print(distances)