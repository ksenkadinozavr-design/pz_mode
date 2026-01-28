#=========================================================
# PRACTICE: PZ12
# AUTHOR: Студент: ____
# TEACHER: Сидоркин Т.А.
# GROUP:
#=========================================================


def factorial(n):
    ## Рекурсивный факториал
    if n <= 1:
        return 1
    return n * factorial(n - 1)


def sum_digits(n):
    ## Рекурсивная сумма цифр
    n = abs(n)
    if n < 10:
        return n
    return n % 10 + sum_digits(n // 10)


print("PZ12: Рекурсия")
print("1 - Факториал")
print("2 - Сумма цифр")
choice = input("Выберите пункт: ").strip()

if choice == "1":
    n = int(input("Введите n: "))
    print("Факториал:", factorial(n))
elif choice == "2":
    n = int(input("Введите число: "))
    print("Сумма цифр:", sum_digits(n))
else:
    print("Ошибка: неверный выбор")
