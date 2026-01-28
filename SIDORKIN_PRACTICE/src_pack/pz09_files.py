#=========================================================
# PRACTICE: PZ09
# AUTHOR: Студент: ____
# TEACHER: Сидоркин Т.А.
# GROUP:
#=========================================================

import os


def ensure_sample_input(path):
    ## Генерация примерного файла
    if os.path.exists(path):
        return
    sample = [
        "3 3",
        "1 2 3",
        "4 5 6",
        "7 8 9",
    ]
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as file:
        file.write("\n".join(sample))


def read_matrix_from_file(path):
    with open(path, "r", encoding="utf-8") as file:
        lines = [line.strip() for line in file if line.strip()]
    rows, cols = map(int, lines[0].split())
    matrix = []
    for line in lines[1:1 + rows]:
        matrix.append([float(x) for x in line.split()[:cols]])
    return matrix


def format_matrix(matrix):
    return [" ".join(f"{val:g}" for val in row) for row in matrix]


def variant_0(m):
    return [
        f"Сумма элементов: {sum(sum(row) for row in m)}",
        "Транспонированная матрица:",
        *format_matrix(list(map(list, zip(*m))))
    ]


def variant_1(m):
    return [
        f"Максимальный элемент: {max(max(row) for row in m)}",
        f"Минимальный элемент: {min(min(row) for row in m)}",
    ]


def variant_2(m):
    return [
        f"Суммы строк: {[sum(row) for row in m]}",
        f"Суммы столбцов: {[sum(col) for col in zip(*m)]}",
    ]


def variant_3(m):
    diag = [m[i][i] for i in range(min(len(m), len(m[0])))]
    return [
        f"Главная диагональ: {diag}",
        f"Сумма диагонали: {sum(diag)}",
    ]


def variant_4(m):
    above = [str(m[i][j]) for i in range(len(m)) for j in range(len(m[0])) if j > i]
    below = [str(m[i][j]) for i in range(len(m)) for j in range(len(m[0])) if j < i]
    return [
        "Элементы выше диагонали: " + " ".join(above),
        "Элементы ниже диагонали: " + " ".join(below),
    ]


def variant_5(m):
    return [
        f"Среднее по строкам: {[sum(row) / len(row) for row in m]}",
        f"Среднее по столбцам: {[sum(col) / len(col) for col in zip(*m)]}",
    ]


def variant_6(m):
    positives = sum(1 for row in m for val in row if val > 0)
    negatives = sum(1 for row in m for val in row if val < 0)
    return [
        f"Количество положительных: {positives}",
        f"Количество отрицательных: {negatives}",
    ]


def variant_7(m):
    replaced = [[1 if val == 0 else val for val in row] for row in m]
    doubled = [[val * 2 for val in row] for row in m]
    return [
        "Матрица без нулей (0 -> 1):",
        *format_matrix(replaced),
        "Матрица умноженная на 2:",
        *format_matrix(doubled),
    ]


def variant_8(m):
    even_idx = sum(m[i][j] for i in range(len(m)) for j in range(len(m[0])) if (i + j) % 2 == 0)
    odd_idx = sum(m[i][j] for i in range(len(m)) for j in range(len(m[0])) if (i + j) % 2 == 1)
    return [
        f"Сумма элементов с четными индексами: {even_idx}",
        f"Сумма элементов с нечетными индексами: {odd_idx}",
    ]


def variant_9(m):
    return [
        f"Максимум по строкам: {[max(row) for row in m]}",
        f"Минимум по столбцам: {[min(col) for col in zip(*m)]}",
    ]


def variant_10(m):
    non_negative = [[0 if val < 0 else val for val in row] for row in m]
    absolute = [[abs(val) for val in row] for row in m]
    return [
        "Матрица с заменой отрицательных на 0:",
        *format_matrix(non_negative),
        "Матрица с модулем:",
        *format_matrix(absolute),
    ]


def variant_11(m):
    side = [m[i][-(i + 1)] for i in range(min(len(m), len(m[0])))]
    return [
        f"Побочная диагональ: {side}",
        f"Сумма побочной диагонали: {sum(side)}",
    ]


def variant_12(m):
    average = sum(sum(row) for row in m) / (len(m) * len(m[0]))
    count = sum(1 for row in m for val in row if val > average)
    updated = [[val + 1 for val in row] for row in m]
    return [
        f"Количество элементов > среднего: {count}",
        "Матрица с добавлением 1 к каждому:",
        *format_matrix(updated),
    ]


def variant_13(m):
    return [
        f"Сумма элементов первой строки: {sum(m[0])}",
        f"Сумма элементов последней строки: {sum(m[-1])}",
    ]


def variant_14(m):
    return [
        f"Сумма элементов первого столбца: {sum(row[0] for row in m)}",
        f"Сумма элементов последнего столбца: {sum(row[-1] for row in m)}",
    ]


def variant_15(m):
    absolute = [[abs(val) for val in row] for row in m]
    rounded = [[round(val, 2) for val in row] for row in m]
    return [
        "Матрица по модулю:",
        *format_matrix(absolute),
        "Матрица с округлением:",
        *format_matrix(rounded),
    ]


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

base_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.abspath(os.path.join(base_dir, "..", "data_io"))
input_file = os.path.join(data_dir, "ФИО_группа_vvod.txt")
output_file = os.path.join(data_dir, "ФИО_группа_vivod.txt")

ensure_sample_input(input_file)
matrix = read_matrix_from_file(input_file)

print("PZ09: Матрицы из файла")
print("Доступные варианты: 0-15")
choice = input("Выберите вариант: ").strip()

if choice in variants:
    output_lines = variants[choice](matrix)
    with open(output_file, "w", encoding="utf-8") as file:
        file.write("\n".join(output_lines))
    print(f"Результаты записаны в файл: {output_file}")
else:
    print("Ошибка: неверный вариант")
