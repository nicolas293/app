import tkinter as tk
from tkinter.scrolledtext import Frame, ScrolledText

class LineNumberWidget:
    def __init__(self, master):
        self.text_frame = Frame(master)
        self.text_frame.pack(side="left", fill="both", expand=True)

        # Виджет для номеров строк
        self.line_numbers_text = tk.Text(self.text_frame, width=3)
        self.line_numbers_text.pack(side="left", fill="y")

        # Основной текстовый виджет
        self.main_text = ScrolledText(self.text_frame)
        self.main_text.pack(side="left", fill="both", expand=True)

        # Настройка внешнего вида виджета номеров строк
        self.line_numbers_text.config(state="disabled", bg="lightgray")

        # Привязка событий
        self.main_text.bind("<<Modified>>", self.update_line_numbers)
        self.main_text.bind("<KeyRelease>", self.update_line_numbers)
        self.main_text.bind("<MouseWheel>", self.on_scroll)

    def update_line_numbers(self, event=None):
        # Получаем количество строк в основном тексте
        lines = self.main_text.get("1.0", "end-1c").count("\n") + 1

        # Очищаем и обновляем номера строк
        self.line_numbers_text.config(state="normal")
        self.line_numbers_text.delete("1.0", tk.END)
        self.line_numbers_text.insert(tk.END, "\n".join(str(i) for i in range(1, lines + 1)))
        self.line_numbers_text.config(state="disabled")
        # Синхронизируем прокрутку
        self.line_numbers_text.yview_moveto(self.main_text.yview()[0])

    def on_scroll(self, *args):
        self.line_numbers_text.yview_moveto(self.main_text.yview()[0])