import tkinter as tk
from tkinter import Canvas, Menu

def my_calculate_window(parent_window):

    test = tk.Toplevel(parent_window)
    test.title('-0.5v-')

    def circle():
        c.create_oval(x, y, x + 30, y + 30, fill='red')

    def square():
        c.create_rectangle(x, y, x + 30, y + 30, fill='blue')


    def triangle():
        c.create_polygon(x, y, x- 15, y + 30, x + 15, y + 30,
                        fill='green', outline='black')

    def popup(e):
        global x, y
        x = e.x
        y = e.y
        menu.post(e.x_root, e.y_root)

    c = Canvas(test, width=300, height=300)
    c.pack()

    test.bind("<Button-3>", popup)

    menu = Menu(test, tearoff=0)
    menu.add_command(label="Круг", command=circle)
    menu.add_command(label="Квадрат", command=square)
    menu.add_command(label="Треугольник", command=triangle)

    test.mainloop()                
