#=========================================================
# PRACTICE: PZ03
# AUTHOR: Студент: ____
# TEACHER: Сидоркин Т.А.
# GROUP:
#=========================================================

import math


def main_task():
    ## Основная задача
    nums = [int(input("Введите число 1: ")), int(input("Введите число 2: ")), int(input("Введите число 3: "))]
    in_range = [n for n in nums if 1 <= n <= 3]
    print("Числа в интервале [1,3]:", in_range)


def task_1():
    a = int(input("Введите число a: "))
    b = int(input("Введите число b: "))
    print("Большее число:", max(a, b))


def task_2():
    n = int(input("Введите число: "))
    print("Четное" if n % 2 == 0 else "Нечетное")


def task_3():
    n = input("Введите число: ").strip()
    even_digits = "".join(d for d in n if d.isdigit() and int(d) % 2 == 0)
    odd_digits = "".join(d for d in n if d.isdigit() and int(d) % 2 == 1)
    print("Четные цифры:", even_digits)
    print("Нечетные цифры:", odd_digits)


def task_4():
    n = int(input("Введите число: "))
    if n < 2:
        print("Не простое")
        return
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            print("Не простое")
            return
    print("Простое")


def task_5():
    nums = [float(input("Введите число 1: ")), float(input("Введите число 2: ")), float(input("Введите число 3: "))]
    print("Среднее арифметическое:", sum(nums) / 3)


def task_6():
    n = int(input("Введите число: "))
    print("Кратно 7" if n % 7 == 0 else "Не кратно 7")


def task_7():
    year = int(input("Введите год: "))
    leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
    print("Високосный" if leap else "Не високосный")


def task_8():
    month = int(input("Введите номер месяца (1-12): "))
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if 1 <= month <= 12:
        print("Дней:", days[month - 1])
    else:
        print("Ошибка: неверный месяц")


def task_9():
    a = float(input("Введите сторону a: "))
    b = float(input("Введите сторону b: "))
    c = float(input("Введите сторону c: "))
    p = (a + b + c) / 2
    area_sq = p * (p - a) * (p - b) * (p - c)
    if area_sq <= 0:
        print("Ошибка: неверные стороны")
        return
    print("Площадь:", math.sqrt(area_sq))


def task_10():
    a = input("Введите число 1: ").strip()
    b = input("Введите число 2: ").strip()
    c = input("Введите число 3: ").strip()
    print("Все равны" if a == b == c else "Не равны")


def task_11():
    age = int(input("Введите возраст: "))
    if age < 0:
        print("Ошибка: возраст не может быть отрицательным")
    elif age < 18:
        print("Несовершеннолетний")
    else:
        print("Совершеннолетний")


def task_12():
    n = float(input("Введите число: "))
    if n > 0:
        print("Положительное")
    elif n < 0:
        print("Отрицательное")
    else:
        print("Ноль")


def task_13():
    year = int(input("Введите год: "))
    leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
    print("Високосный" if leap else "Не високосный")
    print("Февраль дней:", 29 if leap else 28)


def task_14():
    x = float(input("Введите x: "))
    y = float(input("Введите y: "))
    inside = 0 <= x <= 5 and 0 <= y <= 5
    print("Точка внутри квадрата" if inside else "Точка вне квадрата")


def task_15():
    a = float(input("Введите число a: "))
    b = float(input("Введите число b: "))
    print("Сумма:", a + b)
    print("Разность:", a - b)


def task_16():
    n = int(input("Введите число: "))
    print("Кратно 3 и 5" if n % 3 == 0 and n % 5 == 0 else "Не кратно 3 и 5")


def task_17():
    year = int(input("Введите год: "))
    print("Вековый год" if year % 100 == 0 else "Не вековый год")


def task_18():
    value = input("Введите число: ").strip()
    if "." in value:
        print("Дробное")
    else:
        print("Целое")


tasks = {
    "0": ("Основная задача", main_task),
    "1": ("Сравнение двух чисел", task_1),
    "2": ("Четность числа", task_2),
    "3": ("Четные и нечетные цифры", task_3),
    "4": ("Проверка на простоту", task_4),
    "5": ("Среднее арифметическое", task_5),
    "6": ("Кратность 7", task_6),
    "7": ("Високосный год", task_7),
    "8": ("Дни в месяце", task_8),
    "9": ("Формула Герона", task_9),
    "10": ("Равенство трех чисел", task_10),
    "11": ("Возрастная проверка", task_11),
    "12": ("Положительное/отрицательное", task_12),
    "13": ("Високосность + февраль", task_13),
    "14": ("Точка в квадрате", task_14),
    "15": ("Сумма и разность", task_15),
    "16": ("Кратность 3 и 5", task_16),
    "17": ("Вековый год", task_17),
    "18": ("Целое или дробное", task_18),
}

print("PZ03: Условия")
for key, (title, _) in tasks.items():
    print(f"{key} - {title}")
choice = input("Выберите задачу: ").strip()

if choice in tasks:
    tasks[choice][1]()
else:
    print("Ошибка: неверный выбор")
