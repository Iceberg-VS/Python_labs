import math

# Функция с использованием рекурсии
def recursia(n):
    if n == 1:
        return math.sqrt(3)
    else:
        return math.sqrt(3+recursia(n-1))

# Функция без использования рекурсии
def nerekurcia(n):
    result = math.sqrt(3)
    i=0
    for i in range(n-1):
        result = math.sqrt(result+3)
    return result

n = 3  # Заданное значение n

# Вызов функций и вывод результатов
result1 = recursia(n)
result2 = nerekurcia(n)

print(f"{n} с использованием рекурсии: {result1}")
print(f"{n} без использования рекурсии: {result2}")
def pukpuk(list1,list2):
    c=[]
    for i in list2:
        for j in list1:
            if i==j:
                c.append(i)
    return c
func1=[2, 3, 4, 6, 8]
func2=[1, 2, 3, 4]
print(pukpuk(func1,func2))
func3=[5, 8, 2]
func4=[2, 9, 1]
print(pukpuk(func3,func4))
func5=[5, 8, 2]
func6=[7, 4]
print(pukpuk(func5,func6))

def pukpuk(list1,list2):
    c=[]
    for i in list2:
        for j in list1:
            if i==j:
                c.append(i)
    return c