#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# в саду сорвали цветы
garden = ('ромашка', 'роза', 'одуванчик', 'ромашка', 'гладиолус', 'подсолнух', 'роза', )

# на лугу сорвали цветы
meadow = ('клевер', 'одуванчик', 'ромашка', 'клевер', 'мак', 'одуванчик', 'ромашка', )

# создайте множество цветов, произрастающих в саду и на лугу
garden_set = set(garden)
meadow_set = set(meadow)
# TODO здесь ваш код
result_set = garden_set | meadow_set
# выведите на консоль все виды цветов
print(result_set)
# TODO здесь ваш код

# выведите на консоль те, которые растут и там и там
# TODO здесь ваш код
intersection = garden_set & meadow_set
print(intersection)
# выведите на консоль те, которые растут в саду, но не растут на лугу
# TODO здесь ваш код
difference1_set = garden_set - meadow_set
print(difference1_set)
# выведите на консоль те, которые растут на лугу, но не растут в саду
difference2_set = meadow_set - garden_set
print(difference2_set)
# TODO здесь ваш код
