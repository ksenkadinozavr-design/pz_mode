#=========================================================
# PRACTICE: PZ05
# AUTHOR: Студент: ____
# TEACHER: Сидоркин Т.А.
# GROUP:
#=========================================================

import string


def variant_0(text):
    ## Палиндром
    cleaned = "".join(ch.lower() for ch in text if not ch.isspace())
    print("Палиндром" if cleaned == cleaned[::-1] else "Не палиндром")


def variant_1(text):
    ## Количество слов
    words = [w for w in text.split() if w]
    print("Количество слов:", len(words))


def variant_2(text):
    ## Количество гласных
    vowels = "аеёиоуыэюяaeiou"
    count = sum(1 for ch in text.lower() if ch in vowels)
    print("Гласных:", count)


def variant_3(text):
    ## Количество согласных
    vowels = "аеёиоуыэюяaeiou"
    count = sum(1 for ch in text.lower() if ch.isalpha() and ch not in vowels)
    print("Согласных:", count)


def variant_4(text):
    ## Самое длинное слово
    words = [w.strip(string.punctuation) for w in text.split()]
    longest = max(words, key=len, default="")
    print("Самое длинное слово:", longest)


def variant_5(text):
    ## Самое короткое слово
    words = [w.strip(string.punctuation) for w in text.split() if w.strip(string.punctuation)]
    shortest = min(words, key=len, default="")
    print("Самое короткое слово:", shortest)


def variant_6(text):
    ## Замена пробелов
    print(text.replace(" ", "_"))


def variant_7(text):
    ## Удаление цифр
    print("".join(ch for ch in text if not ch.isdigit()))


def variant_8(text):
    ## Удаление знаков препинания
    table = str.maketrans("", "", string.punctuation)
    print(text.translate(table))


def variant_9(text):
    ## Обратный порядок
    print(text[::-1])


def variant_10(text):
    ## Количество подстроки
    sub = input("Введите подстроку: ")
    print("Вхождений:", text.count(sub))


def variant_11(text):
    ## Является ли числом
    cleaned = text.strip()
    is_number = cleaned.replace(".", "", 1).replace("-", "", 1).isdigit()
    print("Число" if is_number else "Не число")


def variant_12(text):
    ## Заглавные буквы
    print(" ".join(word.capitalize() for word in text.split()))


def variant_13(text):
    ## Символы в скобках
    start = text.find("(")
    end = text.find(")", start + 1)
    if start != -1 and end != -1:
        print(text[start + 1:end])
    else:
        print("Скобки не найдены")


def variant_14(text):
    ## Удаление повторов
    seen = set()
    result = []
    for ch in text:
        if ch not in seen:
            seen.add(ch)
            result.append(ch)
    print("".join(result))


def variant_15(text):
    ## Удаление слов короче 3
    words = [w for w in text.split() if len(w) >= 3]
    print(" ".join(words))


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

print("PZ05: Строки")
print("Доступные варианты: 0-15")
choice = input("Выберите вариант: ").strip()
text_input = input("Введите строку: ")

if choice in variants:
    variants[choice](text_input)
else:
    print("Ошибка: неверный вариант")
