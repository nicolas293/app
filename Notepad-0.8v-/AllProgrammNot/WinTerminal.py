import tkinter as tk
import os

def execute_command():
    command = entry.get()
    try:
        output = os.popen(command).read()
        text.insert(tk.END, output)
    except Exception as e:
        text.insert(tk.END, f"Ошибка: {str(e)}\n")

def create_terminal_window():
    # Создаем дочернее окно
    terminal_window = tk.Toplevel()
    terminal_window.title("Терминал")
    terminal_window.geometry("800x600")
    
    # Создаем текстовый виджет для вывода
    global text
    text = tk.Text(terminal_window, bg="black", fg="white", font=("Consolas", 12))
    text.pack(expand=True, fill=tk.BOTH)
    
    # Создаем поле ввода команд
    global entry
    entry = tk.Entry(terminal_window, bg="black", fg="white", font=("Consolas", 12))
    entry.pack(fill=tk.X)

