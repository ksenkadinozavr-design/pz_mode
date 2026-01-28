#=========================================================
# PRACTICE: PZ06
# AUTHOR: Студент: ____
# TEACHER: Сидоркин Т.А.
# GROUP:
#=========================================================

import math


def read_array():
    n = int(input("Введите размер массива: "))
    arr = []
    for i in range(n):
        arr.append(float(input(f"Элемент {i + 1}: ")))
    return arr


def variant_0():
    x = read_array()
    m = float(input("Введите M: "))
    y = [val for val in x if abs(val) > m]
    print("M:", m)
    print("X:", x)
    print("Y:", y)
    x = [abs(val) if val < 0 else val for val in x]
    print("X без отрицательных:", x)


def variant_1():
    x = read_array()
    print("Максимальный элемент:", max(x))
    print("Обратный порядок:", list(reversed(x)))
    avg = sum(x) / len(x) if x else 0
    x = [avg if val == 0 else val for val in x]
    print("Замена нулей средним:", x)


def variant_2():
    x = read_array()
    positives = [val for val in x if val > 0]
    print("Положительные элементы:", positives)
    avg = sum(x) / len(x) if x else 0
    x = [val for val in x if val != avg]
    print("Без элементов равных среднему:", x)


def variant_3():
    x = read_array()
    total = sum(val for val in x if val < 0)
    print("Сумма элементов < 0:", total)
    x = [val * 2 if val < 15 else val for val in x]
    print("Элементы < 15 удвоены:", x)


def variant_4():
    x = read_array()
    count_even = sum(1 for val in x if val % 2 == 0)
    print("Количество четных:", count_even)
    x = [0 if val % 3 == 0 else val for val in x]
    print("Элементы, кратные 3, заменены на 0:", x)


def variant_5():
    x = read_array()
    min_val = min(x)
    print("Минимальный элемент:", min_val)
    x = [val + min_val for val in x]
    print("Массив после прибавления min:", x)


def variant_6():
    x = read_array()
    print("Количество отрицательных:", sum(1 for val in x if val < 0))
    x = [abs(val) ** 0.5 if val >= 0 else val for val in x]
    print("Корни неотрицательных:", x)


def variant_7():
    x = read_array()
    print("Сумма четных:", sum(val for val in x if val % 2 == 0))
    x = [val if val >= 0 else 0 for val in x]
    print("Отрицательные заменены на 0:", x)


def variant_8():
    x = read_array()
    max_val = max(x)
    print("Максимальный элемент:", max_val)
    x = [val / max_val if max_val != 0 else 0 for val in x]
    print("Нормализованный массив:", x)


def variant_9():
    x = read_array()
    print("Среднее арифметическое:", sum(x) / len(x) if x else 0)
    x = [val for val in x if val != 0]
    print("Без нулей:", x)


def variant_10():
    x = read_array()
    print("Элементы > среднего:", [val for val in x if val > sum(x) / len(x)])
    x = [val ** 2 for val in x]
    print("Квадраты элементов:", x)


def variant_11():
    x = read_array()
    print("Произведение элементов:", math.prod(x) if x else 1)
    x = [val + i for i, val in enumerate(x)]
    print("Элементы + индекс:", x)


def variant_12():
    x = read_array()
    print("Сумма элементов на нечетных позициях:", sum(val for i, val in enumerate(x) if i % 2 == 1))
    x = [val for val in x if val >= 0]
    print("Только неотрицательные:", x)


def variant_13():
    x = read_array()
    print("Минимум по модулю:", min(x, key=lambda v: abs(v)))
    x = [val * -1 for val in x]
    print("Знаки изменены:", x)


def variant_14():
    x = read_array()
    print("Максимум по модулю:", max(x, key=lambda v: abs(v)))
    x = [val for val in x if val % 5 != 0]
    print("Удалены элементы кратные 5:", x)


def variant_15():
    x = read_array()
    print("Количество элементов > 10:", sum(1 for val in x if val > 10))
    x = [val - 1 for val in x]
    print("Каждый элемент уменьшен на 1:", x)


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

print("PZ06: Массивы")
print("Доступные варианты: 0-15")
choice = input("Выберите вариант: ").strip()

if choice in variants:
    variants[choice]()
else:
    print("Ошибка: неверный вариант")
