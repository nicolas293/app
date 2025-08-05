import tkinter as tk
from tkinter import ttk

class VirtualKeyboard:
    def __init__(self, root):
        self.root = root
        self.root.title("Экранная клавиатура")
        
        # Основные параметры клавиатуры
        self.keys = [
            ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P'],
            ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L'],
            ['Z', 'X', 'C', 'V', 'B', 'N', 'M'],
            ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'],
            ['Backspace', 'Enter']
        ]
        
        # Создаем фрейм для клавиатуры
        self.keyboard_frame = ttk.Frame(root)
        self.keyboard_frame.pack(padx=10, pady=10)
        
        # Создаем поле ввода
        self.entry = ttk.Entry(root, width=50, font=("Arial", 14))
        self.entry.pack(pady=20)
        
        # Создаем кнопки клавиатуры
        self.create_buttons()

    def create_buttons(self):
        row_num = 0
        for row in self.keys:
            col_num = 0
            for key in row:
                if key == 'Backspace':
                    btn = ttk.Button(self.keyboard_frame, text=key, width=10,
                                    command=self.backspace)
                elif key == 'Enter':
                    btn = ttk.Button(self.keyboard_frame, text=key, width=10,
                                    command=self.enter)
                else:
                    btn = ttk.Button(self.keyboard_frame, text=key, width=5,
                                    command=lambda k=key: self.insert_text(k))
                btn.grid(row=row_num, column=col_num, padx=2, pady=2)
                col_num += 1
            row_num += 1

    def insert_text(self, char):
        self.entry.insert(tk.END, char)

    def backspace(self):
        current_text = self.entry.get()
        self.entry.delete(0, tk.END)
        self.entry.insert(0, current_text[:-1])

    def enter(self):
        print(f"Введено: {self.entry.get()}")
        self.entry.delete(0, tk.END)

class Application:
    def __init__(self):
        self.root = tk.Tk()
        self.root.resizable(0, 0)
        self.root.title("Основное приложение")
        self.root.geometry("640x300")
        
        # Создаем экземпляр клавиатуры
        self.keyboard = VirtualKeyboard(self.root)
        
        # Добавляем кнопку для показа/скрытия клавиатуры
        self.show_keyboard_btn = ttk.Button(self.root, text="Показать клавиатуру",
                                           command=self.toggle_keyboard)
        self.show_keyboard_btn.pack(pady=10)

        
        # Флаг видимости клавиатуры
        self.keyboard_visible = False

    def toggle_keyboard(self):
        if self.keyboard_visible:
            self.keyboard.keyboard_frame.pack_forget()
            self.keyboard.entry.pack_forget()
            self.show_keyboard_btn.config(text="Показать клавиатуру")
            self.keyboard_visible = False
        else:
            self.keyboard.keyboard_frame.pack(padx=10, pady=10)
            self.keyboard.entry.pack(pady=20)
            self.show_keyboard_btn.config(text="Скрыть клавиатуру")
            self.keyboard_visible = True

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = Application()