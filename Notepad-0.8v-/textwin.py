import tkinter as tk

class StatefulFrame(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.create_widgets()
        self.state = {}  # Словарь для хранения состояния

    def create_widgets(self):
        self.entry = tk.Entry(self)
        self.entry.pack()
        self.checkbox_var = tk.IntVar()
        self.checkbox = tk.Checkbutton(self, variable=self.checkbox_var, text="Checkbox")
        self.checkbox.pack()
        self.save_button = tk.Button(self, text="Сохранить состояние", command=self.save_state)
        self.save_button.pack()
        self.load_button = tk.Button(self, text="Загрузить состояние", command=self.load_state)
        self.load_button.pack()

    def save_state(self):
        # Сохраняем текущее состояние виджетов
        self.state['entry_text'] = self.entry.get()
        self.state['checkbox_value'] = self.checkbox_var.get()
        print("Состояние сохранено:", self.state)

    def load_state(self):
        # Восстанавливаем сохраненное состояние
        if self.state:
            self.entry.delete(0, tk.END)
            self.entry.insert(0, self.state['entry_text'])
            self.checkbox_var.set(self.state['checkbox_value'])
            print("Состояние восстановлено")

# Пример использования
root = tk.Tk()
frame = StatefulFrame(root)
frame.pack(fill=tk.BOTH, expand=True)
root.mainloop()