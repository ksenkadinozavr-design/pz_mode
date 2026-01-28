#=========================================================
# PRACTICE: PZ11
# AUTHOR: Студент: ____
# TEACHER: Сидоркин Т.А.
# GROUP:
#=========================================================

import json
import os
import tkinter as tk
from tkinter import ttk, messagebox

import requests


def fetch_repo():
    ## Запрос GitHub API
    repo_name = entry_repo.get().strip()
    if not repo_name:
        messagebox.showerror("Ошибка", "Введите название репозитория")
        return
    url = f"https://api.github.com/repos/{repo_name}"
    try:
        response = requests.get(url, timeout=10)
    except requests.exceptions.RequestException:
        messagebox.showerror("Ошибка", "Проблема с сетью")
        return
    if response.status_code == 404:
        messagebox.showerror("Ошибка", "Репозиторий не найден")
        return
    if response.status_code != 200:
        messagebox.showerror("Ошибка", f"HTTP ошибка: {response.status_code}")
        return

    data = response.json()
    result = {
        "company": data.get("owner", {}).get("company"),
        "created_at": data.get("created_at"),
        "email": data.get("owner", {}).get("email"),
        "id": data.get("id"),
        "name": data.get("name"),
        "url": data.get("html_url"),
    }

    if any(value in (None, "") for value in result.values()):
        messagebox.showwarning("Предупреждение", "Некоторые поля отсутствуют")

    output_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data_io", "result_repo.json")
    with open(output_path, "w", encoding="utf-8") as file:
        json.dump(result, file, ensure_ascii=False, indent=2)
    messagebox.showinfo("Готово", f"Данные сохранены в {output_path}")


root = tk.Tk()
root.title("GitHub API")
root.geometry("400x150")

label_repo = ttk.Label(root, text="Repository name (owner/repo):")
label_repo.pack(padx=10, pady=5)

entry_repo = ttk.Entry(root)
entry_repo.pack(fill="x", padx=10, pady=5)

button_fetch = ttk.Button(root, text="Получить", command=fetch_repo)
button_fetch.pack(pady=10)

root.mainloop()
