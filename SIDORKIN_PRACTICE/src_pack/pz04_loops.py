#=========================================================
# PRACTICE: PZ04
# AUTHOR: Студент: ____
# TEACHER: Сидоркин Т.А.
# GROUP:
#=========================================================


def task_1():
    a = int(input("Введите A: "))
    b = int(input("Введите B: "))
    for n in range(a, b + 1):
        print(n, end=" ")
    print()


def task_2():
    a = int(input("Введите A: "))
    b = int(input("Введите B: "))
    if a <= b:
        for n in range(a, b + 1):
            print(n, end=" ")
    else:
        for n in range(a, b - 1, -1):
            print(n, end=" ")
    print()


def task_3():
    a = int(input("Введите A: "))
    b = int(input("Введите B: "))
    for n in range(b if b % 2 == 1 else b - 1, a - 1, -2):
        print(n, end=" ")
    print()


def task_4():
    n = int(input("Введите N: "))
    total = 0
    for _ in range(n):
        total += float(input("Введите число: "))
    print("Сумма:", total)


def task_5():
    n = int(input("Введите n: "))
    total = 0
    for i in range(1, n + 1):
        total += i ** 3
    print("Сумма кубов:", total)


def task_6():
    n = int(input("Введите n: "))
    fact = 1
    for i in range(2, n + 1):
        fact *= i
    print("Факториал:", fact)


def task_7():
    n = int(input("Введите n: "))
    total = 0
    fact = 1
    for i in range(1, n + 1):
        fact *= i
        total += fact
    print("Сумма факториалов:", total)


def task_8():
    n = int(input("Введите n (<=9): "))
    for i in range(1, n + 1):
        print("".join(str(j) for j in range(1, i + 1)))


def task_9():
    n = int(input("Введите n: "))
    a, b = 1, 1
    total = 0
    for _ in range(n):
        total += a
        a, b = b, a + b
    print("Сумма чисел Фибоначчи:", total)


def task_10():
    n = int(input("Введите n: "))
    k = int(input("Введите k: "))
    a, b = 1, 1
    total = 0
    for i in range(1, k + n):
        if i >= k:
            total += a
        a, b = b, a + b
    print("Сумма Фибоначчи с k-го:", total)


tasks = {
    "1": task_1,
    "2": task_2,
    "3": task_3,
    "4": task_4,
    "5": task_5,
    "6": task_6,
    "7": task_7,
    "8": task_8,
    "9": task_9,
    "10": task_10,
}

print("PZ04: Циклы")
for i in range(1, 11):
    print(f"{i} - Задача {i}")
choice = input("Выберите задачу: ").strip()

if choice in tasks:
    tasks[choice]()
else:
    print("Ошибка: неверный выбор")
