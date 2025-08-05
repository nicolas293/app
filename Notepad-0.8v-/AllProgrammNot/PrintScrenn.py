import tkinter as tk
from tkinter import messagebox
import pyautogui
import time

def take_screenshot():
    try:
        # Скрываем окно на время создания скриншота
        root.withdraw()
        
        # Генерируем уникальное имя файла
        timestamp = int(time.time())
        filename = f"screenshot_{timestamp}.png"
        
        # Делаем скриншот
        screenshot = pyautogui.screenshot(filename)
        
        # Показываем сообщение об успешном сохранении
        messagebox.showinfo("Скриншот сохранен", f"Файл сохранен как {filename}")
        
        # Восстанавливаем окно
        # root.deiconify()
        
    except Exception as e:
        messagebox.showerror("Ошибка", f"Произошла ошибка: {str(e)}")
        # root.deiconify()

# Создаем основное окно
root = tk.Tk()
root.title("Приложение для скриншотов")
root.geometry("400x200")

# Добавляем кнопку для создания скриншота
screenshot_button = tk.Button(
    root, 
    text="Сделать скриншот", 
    font=("Arial", 14),
    command=take_screenshot,
    bg="lightblue",
    fg="black"
)
screenshot_button.pack(pady=20)

# Добавляем кнопку выхода
exit_button = tk.Button(
    root, 
    text="Выход", 
    font=("Arial", 14),
    command=root.destroy,
    bg="lightcoral",
    fg="white"
)
exit_button.pack(pady=10)

root.mainloop()
