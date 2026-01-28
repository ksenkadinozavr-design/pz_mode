#=========================================================
# PRACTICE: PZ10
# AUTHOR: Студент: ____
# TEACHER: Сидоркин Т.А.
# GROUP:
#=========================================================

import tkinter as tk
from tkinter import ttk, messagebox, filedialog


def calculate():
    ## Калькулятор
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
    except ValueError:
        messagebox.showerror("Ошибка", "Введите корректные числа")
        return
    op = operation.get()
    if op == "+":
        result = a + b
    elif op == "-":
        result = a - b
    elif op == "*":
        result = a * b
    elif op == "/":
        if b == 0:
            messagebox.showerror("Ошибка", "Деление на ноль")
            return
        result = a / b
    else:
        messagebox.showerror("Ошибка", "Выберите операцию")
        return
    result_var.set(f"Результат: {result}")


def show_checks():
    ## Чекбоксы
    selected = []
    if var1.get():
        selected.append("Вариант 1")
    if var2.get():
        selected.append("Вариант 2")
    if var3.get():
        selected.append("Вариант 3")
    text = ", ".join(selected) if selected else "Ничего не выбрано"
    messagebox.showinfo("Выбор", text)


def open_file():
    ## Открыть файл
    path = filedialog.askopenfilename(title="Открыть файл", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if not path:
        return
    with open(path, "r", encoding="utf-8") as file:
        content = file.read()
    text_box.delete("1.0", tk.END)
    text_box.insert(tk.END, content)


root = tk.Tk()
root.title("ФИО автора")
root.geometry("700x400")

notebook = ttk.Notebook(root)
notebook.pack(expand=True, fill="both")

## Вкладка 1
frame1 = ttk.Frame(notebook)
notebook.add(frame1, text="Калькулятор")

entry_a = ttk.Entry(frame1)
entry_b = ttk.Entry(frame1)
operation = tk.StringVar(value="+")
operations = ttk.Combobox(frame1, textvariable=operation, values=["+", "-", "*", "/"], state="readonly")

calc_button = ttk.Button(frame1, text="Вычислить", command=calculate)
result_var = tk.StringVar(value="Результат: ")
result_label = ttk.Label(frame1, textvariable=result_var)

entry_a.grid(row=0, column=0, padx=5, pady=5, sticky="ew")
operations.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
entry_b.grid(row=0, column=2, padx=5, pady=5, sticky="ew")
calc_button.grid(row=1, column=0, columnspan=3, padx=5, pady=5)
result_label.grid(row=2, column=0, columnspan=3, padx=5, pady=5)

for i in range(3):
    frame1.columnconfigure(i, weight=1)

## Вкладка 2
frame2 = ttk.Frame(notebook)
notebook.add(frame2, text="Чекбоксы")

var1 = tk.BooleanVar()
var2 = tk.BooleanVar()
var3 = tk.BooleanVar()

check1 = ttk.Checkbutton(frame2, text="Вариант 1", variable=var1)
check2 = ttk.Checkbutton(frame2, text="Вариант 2", variable=var2)
check3 = ttk.Checkbutton(frame2, text="Вариант 3", variable=var3)
check_button = ttk.Button(frame2, text="Показать выбор", command=show_checks)

check1.pack(anchor="w", padx=10, pady=5)
check2.pack(anchor="w", padx=10, pady=5)
check3.pack(anchor="w", padx=10, pady=5)
check_button.pack(pady=10)

## Вкладка 3
frame3 = ttk.Frame(notebook)
notebook.add(frame3, text="Файл")

text_box = tk.Text(frame3, wrap="word")
text_box.pack(expand=True, fill="both", padx=5, pady=5)

menu_bar = tk.Menu(root)
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Открыть файл", command=open_file)
menu_bar.add_cascade(label="Файл", menu=file_menu)
root.config(menu=menu_bar)

root.mainloop()
