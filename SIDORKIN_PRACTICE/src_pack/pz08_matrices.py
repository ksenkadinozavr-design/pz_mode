#=========================================================
# PRACTICE: PZ08
# AUTHOR: Студент: ____
# TEACHER: Сидоркин Т.А.
# GROUP:
#=========================================================


def read_matrix():
    rows = int(input("Введите число строк: "))
    cols = int(input("Введите число столбцов: "))
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(float(input(f"Элемент [{i + 1},{j + 1}]: ")))
        matrix.append(row)
    return matrix


def print_matrix(matrix):
    for row in matrix:
        print(" ".join(f"{val:g}" for val in row))


def variant_0():
    m = read_matrix()
    print("Сумма элементов:", sum(sum(row) for row in m))
    print("Транспонированная матрица:")
    print_matrix(list(map(list, zip(*m))))


def variant_1():
    m = read_matrix()
    print("Максимальный элемент:", max(max(row) for row in m))
    print("Минимальный элемент:", min(min(row) for row in m))


def variant_2():
    m = read_matrix()
    print("Суммы строк:", [sum(row) for row in m])
    print("Суммы столбцов:", [sum(col) for col in zip(*m)])


def variant_3():
    m = read_matrix()
    diag = [m[i][i] for i in range(min(len(m), len(m[0])))]
    print("Главная диагональ:", diag)
    print("Сумма диагонали:", sum(diag))


def variant_4():
    m = read_matrix()
    print("Элементы выше диагонали:")
    for i in range(len(m)):
        for j in range(len(m[0])):
            if j > i:
                print(m[i][j], end=" ")
    print()
    print("Элементы ниже диагонали:")
    for i in range(len(m)):
        for j in range(len(m[0])):
            if j < i:
                print(m[i][j], end=" ")
    print()


def variant_5():
    m = read_matrix()
    print("Среднее по строкам:", [sum(row) / len(row) for row in m])
    print("Среднее по столбцам:", [sum(col) / len(col) for col in zip(*m)])


def variant_6():
    m = read_matrix()
    print("Количество положительных:", sum(1 for row in m for val in row if val > 0))
    print("Количество отрицательных:", sum(1 for row in m for val in row if val < 0))


def variant_7():
    m = read_matrix()
    print("Матрица без нулей (0 -> 1):")
    updated = [[1 if val == 0 else val for val in row] for row in m]
    print_matrix(updated)
    print("Матрица умноженная на 2:")
    print_matrix([[val * 2 for val in row] for row in m])


def variant_8():
    m = read_matrix()
    print("Сумма элементов с четными индексами:", sum(m[i][j] for i in range(len(m)) for j in range(len(m[0])) if (i + j) % 2 == 0))
    print("Сумма элементов с нечетными индексами:", sum(m[i][j] for i in range(len(m)) for j in range(len(m[0])) if (i + j) % 2 == 1))


def variant_9():
    m = read_matrix()
    print("Максимум по строкам:", [max(row) for row in m])
    print("Минимум по столбцам:", [min(col) for col in zip(*m)])


def variant_10():
    m = read_matrix()
    print("Матрица с заменой отрицательных на 0:")
    print_matrix([[0 if val < 0 else val for val in row] for row in m])
    print("Матрица с модулем:")
    print_matrix([[abs(val) for val in row] for row in m])


def variant_11():
    m = read_matrix()
    print("Побочная диагональ:", [m[i][-(i + 1)] for i in range(min(len(m), len(m[0])))] )
    print("Сумма побочной диагонали:", sum(m[i][-(i + 1)] for i in range(min(len(m), len(m[0])))))


def variant_12():
    m = read_matrix()
    print("Количество элементов > среднего:", sum(1 for row in m for val in row if val > sum(sum(row) for row in m) / (len(m) * len(m[0]))))
    print("Матрица с добавлением 1 к каждому:")
    print_matrix([[val + 1 for val in row] for row in m])


def variant_13():
    m = read_matrix()
    print("Сумма элементов первой строки:", sum(m[0]))
    print("Сумма элементов последней строки:", sum(m[-1]))


def variant_14():
    m = read_matrix()
    print("Сумма элементов первого столбца:", sum(row[0] for row in m))
    print("Сумма элементов последнего столбца:", sum(row[-1] for row in m))


def variant_15():
    m = read_matrix()
    print("Матрица по модулю:")
    print_matrix([[abs(val) for val in row] for row in m])
    print("Матрица с округлением:")
    print_matrix([[round(val, 2) for val in row] for row in m])


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

print("PZ08: Матрицы")
print("Доступные варианты: 0-15")
choice = input("Выберите вариант: ").strip()

if choice in variants:
    variants[choice]()
else:
    print("Ошибка: неверный вариант")
