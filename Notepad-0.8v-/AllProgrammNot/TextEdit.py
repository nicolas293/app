import tkinter as tk
from tkinter.scrolledtext import Frame, ScrolledText

win = tk.Tk()


class ConTins():
    def __init__(self, master):

        self.colors = ['green', 'blue']
        self.color_index = 0

        self.text_frame = Frame(master)
        self.text_frame.pack(side="left", fill="both")

        self.line_number_text = tk.Text(self.text_frame, width=3)
        self.line_number_text.pack(side='left', fill="y")

        self.main_text = ScrolledText(self.text_frame)
        self.main_text.pack(side='left', fill='both')

        self.line_number_text.config(state='disabled', bg="lightgray")

        def update_line_numbers(event=None):
            lines = self.main_text.get("1.0", "end-1c").count('\n') + 1

            self.line_number_text.config(state="normal")
            self.line_number_text.delete("1.0", tk.END)
            self.line_number_text.insert(tk.END, "\n".join(str(i) for i in range(1, lines + 1)))
            self.line_number_text.config(state="disabled") 

            self.line_number_text.yview_moveto(self.main_text.yview()[0])

        def color_bg():
            global color_index
            self.main_text.config(bg=self.colors[self.color_index])
            self.color_index = (self.color_index + 1) % len(self.colors)

        self.main_text.bind("<<Modified>>", update_line_numbers)
        self.main_text.bind("<KeyRelease>", update_line_numbers)

        self.edit = tk.Menu(tearoff=0)
        self.edit.add_command(label='Color Fon', command=color_bg)

        menu = tk.Menu()
        menu.add_cascade(label='File')
        menu.add_cascade(label='Edit', menu=self.edit)
        menu.add_cascade(label='Info')
        win.config(menu=menu)



       