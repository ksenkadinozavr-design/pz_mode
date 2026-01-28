#=========================================================
# PRACTICE: PZ02
# AUTHOR: Студент: ____
# TEACHER: Сидоркин Т.А.
# GROUP:
#=========================================================

import math


def part_a():
    ## Часть А
    x = float(input("Введите x: "))
    t = float(input("Введите t: "))
    if t <= 0:
        print("Ошибка: t должно быть больше 0 для sqrt(t).")
        return
    denom = math.sqrt(t) - abs(math.sin(t))
    if denom == 0:
        print("Ошибка: деление на ноль в части А.")
        return
    z = ((9 * math.pi * t + 10 * math.cos(x)) / denom) * math.exp(x)
    print(f"Z = {z:.2f}")


def part_b():
    ## Часть Б
    print("Выберите формулу 1-5:")
    choice = input("Номер формулы: ").strip()
    x = float(input("Введите x: "))
    y = float(input("Введите y: "))
    z = float(input("Введите z: "))

    if choice == "1":
        denom = 0.5 + math.sin(y) ** 2
        if denom == 0 or (3 - z ** 2 / 5) == 0:
            print("Ошибка: деление на ноль.")
            return
        s = (2 * math.cos(x - 2 / 3)) / denom * (1 + z ** 2 / (3 - z ** 2 / 5))
    elif choice == "2":
        denom = x ** 2 + y ** 2 + 2
        if denom == 0:
            print("Ошибка: деление на ноль.")
            return
        s = math.copysign(abs(9 + (x - y) ** 2) ** (1 / 3), 9 + (x - y) ** 2) / denom
        s -= math.exp(abs(x - y)) * math.tan(z) ** 3
    elif choice == "3":
        denom = abs(x - 2 * y / (1 + x ** 2 * y ** 2))
        if denom == 0 or z == 0:
            print("Ошибка: деление на ноль.")
            return
        s = (1 + math.sin(x + y) ** 2) / denom * (x ** abs(y))
        s += math.cos(math.atan(1 / z)) ** 2
    elif choice == "4":
        s = abs(math.cos(x) - math.cos(y)) ** (1 + 2 * math.sin(y) ** 2)
        s *= (1 + z + z ** 2 / 2 + z ** 3 / 3 + z ** 4 / 4)
    elif choice == "5":
        if y <= 0:
            print("Ошибка: y должно быть больше 0 для логарифма.")
            return
        s = math.log(y ** (-math.sqrt(abs(x)))) * (x - y / 2)
        s += math.sin(math.atan(z)) ** 2
    else:
        print("Ошибка: выбран неверный номер формулы.")
        return

    print(f"s = {s:.4f}")


print("PZ02: Вычисление выражений")
print("1 - Часть А")
print("2 - Часть Б")
mode = input("Выберите часть (1/2): ").strip()

if mode == "1":
    part_a()
elif mode == "2":
    part_b()
else:
    print("Ошибка: неверный выбор.")
