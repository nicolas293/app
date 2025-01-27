import tkinter as tk
from tkinter import ttk
import time
import threading

def windowsOpenWin(parent_window):
    def start_timer():
        try:
            seconds = int(entry.get())
            if seconds <= 0:
                raise ValueError
            
            def countdown():
                nonlocal seconds
                while seconds > 0 and not stop_thread.is_set():
                    time.sleep(1)
                    seconds -= 1
                    label.config(text=f"Окно закроется через: {seconds} сек")
                
                if not stop_thread.is_set():
                    auto_window.destroy()
                    parent_window.destroy()

            stop_thread.clear()
            thread = threading.Thread(target=countdown)
            thread.daemon = True
            thread.start()
            
        except ValueError:
            label.config(text="Пожалуйста, введите положительное число")

    def stop_countdown():
        stop_thread.set()
        label.config(text="Таймер остановлен")

    auto_window = tk.Toplevel(parent_window)
    auto_window.title('Авто-закрытие')
    auto_window.geometry('300x150')

    stop_thread = threading.Event()

    frame = ttk.Frame(auto_window, padding="10")
    frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

    entry = ttk.Entry(frame)
    entry.grid(row=0, column=0, padx=5, pady=5)
    entry.insert(0, "10")

    start_button = ttk.Button(frame, text="Старт", command=start_timer)
    start_button.grid(row=0, column=1, padx=5, pady=5)

    stop_button = ttk.Button(frame, text="Стоп", command=stop_countdown)
    stop_button.grid(row=0, column=2, padx=5, pady=5)

    label = ttk.Label(frame, text="Введите количество секунд")
    label.grid(row=1, column=0, columnspan=3, pady=10)