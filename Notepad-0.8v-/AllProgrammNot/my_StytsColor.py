import tkinter as tk
from tkinter import colorchooser as ch
from tkinter import INSERT

def myStytsColor():

    reg = tk.Tk()
    reg.geometry("250x200")
    reg.title("Выбор цвета")

    line_numbers = tk.Text(reg, height=1, width=10)
    line_numbers.pack(pady=5)

    def choose_color():
        color = ch.askcolor()[1]
        if color is not None:
            line_numbers.delete("1.0", "end")
            line_numbers.insert(INSERT, color)
            color_label.config(text=f"Вы выбрали цвет {color}")  
            second_label.config(bg=color)  

    color_button = tk.Button(reg, text="Выбрать цвет", command=choose_color)
    color_label = tk.Label(reg, text="Нажмите кнопку, чтобы выбрать цвет")
    second_label = tk.Label(reg, text="\t\t\t\n\t\t\t")
    color_button.pack(pady=10)
    color_label.pack()
    second_label.pack(pady=10)

    reg.mainloop()