#=========================================================
# PRACTICE: PZ07
# AUTHOR: Студент: ____
# TEACHER: Сидоркин Т.А.
# GROUP:
#=========================================================

import math


def sum_digits(n):
    ## Сумма цифр
    return sum(int(d) for d in str(abs(n)))


def is_even(n):
    ## Проверка четности
    return n % 2 == 0


def gcd(a, b):
    ## НОД
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    ## НОК
    return abs(a * b) // gcd(a, b) if a and b else 0


def triangle_area(a, b, c):
    ## Площадь треугольника
    p = (a + b + c) / 2
    return math.sqrt(p * (p - a) * (p - b) * (p - c))


def variant_0():
    n = int(input("Введите число: "))
    print("Сумма цифр:", sum_digits(n))
    print("Четное" if is_even(n) else "Нечетное")


def variant_1():
    a = int(input("Введите a: "))
    b = int(input("Введите b: "))
    print("НОД:", gcd(a, b))
    print("НОК:", lcm(a, b))


def variant_2():
    a = float(input("Введите a: "))
    b = float(input("Введите b: "))
    c = float(input("Введите c: "))
    if a + b <= c or a + c <= b or b + c <= a:
        print("Ошибка: треугольник не существует")
        return
    print("Площадь:", triangle_area(a, b, c))
    print("Периметр:", a + b + c)


def variant_3():
    r = float(input("Введите радиус: "))
    print("Длина окружности:", 2 * math.pi * r)
    print("Площадь круга:", math.pi * r ** 2)


def variant_4():
    n = int(input("Введите число: "))
    print("Квадрат:", n ** 2)
    print("Куб:", n ** 3)


def variant_5():
    a = float(input("Введите a: "))
    b = float(input("Введите b: "))
    print("Среднее арифметическое:", (a + b) / 2)
    print("Среднее геометрическое:", math.sqrt(a * b) if a * b >= 0 else "Ошибка")


def variant_6():
    x = float(input("Введите x: "))
    print("sin(x):", math.sin(x))
    print("cos(x):", math.cos(x))


def variant_7():
    n = int(input("Введите n: "))
    print("Факториал:", math.factorial(n))
    print("Сумма 1..n:", n * (n + 1) // 2)


def variant_8():
    a = float(input("Введите a: "))
    b = float(input("Введите b: "))
    print("Минимум:", min(a, b))
    print("Максимум:", max(a, b))


def variant_9():
    x = float(input("Введите x: "))
    print("Модуль:", abs(x))
    print("Квадратный корень:", math.sqrt(x) if x >= 0 else "Ошибка")


def variant_10():
    n = int(input("Введите n: "))
    print("Количество цифр:", len(str(abs(n))))
    print("Первая цифра:", str(abs(n))[0])


def variant_11():
    a = int(input("Введите a: "))
    b = int(input("Введите b: "))
    print("a^b:", pow(a, b))
    print("b^a:", pow(b, a))


def variant_12():
    x = float(input("Введите x: "))
    print("Округление вниз:", math.floor(x))
    print("Округление вверх:", math.ceil(x))


def variant_13():
    n = int(input("Введите n: "))
    print("Сумма четных чисел до n:", sum(i for i in range(2, n + 1, 2)))
    print("Сумма нечетных чисел до n:", sum(i for i in range(1, n + 1, 2)))


def variant_14():
    a = float(input("Введите a: "))
    b = float(input("Введите b: "))
    c = float(input("Введите c: "))
    print("Наибольшее:", max(a, b, c))
    print("Наименьшее:", min(a, b, c))


def variant_15():
    a = int(input("Введите a: "))
    b = int(input("Введите b: "))
    print("Сумма цифр a:", sum_digits(a))
    print("Сумма цифр b:", sum_digits(b))


variants = {
    "0": variant_0,
    "1": variant_1,
    "2": variant_2,
    "3": variant_3,
    "4": variant_4,
    "5": variant_5,
    "6": variant_6,
    "7": variant_7,
    "8": variant_8,
    "9": variant_9,
    "10": variant_10,
    "11": variant_11,
    "12": variant_12,
    "13": variant_13,
    "14": variant_14,
    "15": variant_15,
}

print("PZ07: Функции")
print("Доступные варианты: 0-15")
choice = input("Выберите вариант: ").strip()

if choice in variants:
    variants[choice]()
else:
    print("Ошибка: неверный вариант")
