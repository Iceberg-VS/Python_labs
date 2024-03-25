#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть зашифрованное сообщение

secret_message = [
    'квевтфпп6щ3стмзалтнмаршгб5длгуча',
    'дьсеы6лц2бане4т64ь4б3ущея6втщл6б',
    'т3пплвце1н3и2кд4лы12чф1ап3бкычаь',
    'ьд5фму3ежородт9г686буиимыкучшсал',
    'бсц59мегщ2лятьаьгенедыв9фк9ехб1а',
]
first_word = secret_message[0][3]
second_word = secret_message[1][9:13]
third_word = secret_message[2][5:15:2]
fourth_word = secret_message[3][7:13][::-1]
fifth_word = secret_message[4][16:21][::-1]

# Объединение слов в одно сообщение
decoded_message = first_word+" "+second_word+" "+third_word+" "+fourth_word+" "+fifth_word

# Вывод расшифрованного сообщения
print(decoded_message)
# Нужно его расшифровать и вывести на консоль в удобочитаемом виде.
# Должна получиться фраза на русском языке, например: как два байта переслать.

# Ключ к расшифровке:
#   первое слово - 4-я буква
#   второе слово - буквы с 10 по 13, включительно
#   третье слово - буквы с 6 по 15, включительно, через одну
#   четвертое слово - буквы с 8 по 13, включительно, в обратном порядке
#   пятое слово - буквы с 17 по 21, включительно, в обратном порядке
#
# Обратите вниманме:
#   даны номера букв, а не индексы
#   срез не включает последний индекс
#   подробную информацию об обратных срезах см https://clck.ru/MfEMS
#
# Подсказки:
#   В каждом элементе списка защифровано одно слово.
#   Требуется задать конкретные индексы, например secret_message[3][12:23:4]
#   4е и 5е слова нужно получить за 1 срез
#   Если нужны вычисления и разные пробы - делайте это в консоли пайтона, тут нужен только результат

# TODO вывести расшифрованное сообщение
