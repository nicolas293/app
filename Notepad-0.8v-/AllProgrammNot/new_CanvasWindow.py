import tkinter as tk
from tkinter import colorchooser

def new_window():
    
    def on_canvas_click(event):
        x, y =  event.x, event.y
        canvas.create_oval(x-5, y-5, x+5, y+5, fill=current_color)

    def change_color():
        global current_color
        color = colorchooser.askcolor()
        if color[1] is not None:
            current_color = color[1]

    root = tk.Toplevel()
    root.title('Рисовалка-Python-0.5v')
    root.geometry('350x280')

    current_color = change_color()

    color_button = tk.Button(root, text="Выбрать цвет", command=change_color)
    color_button.pack(side="bottom")

    canvas = tk.Canvas(root, height=800, width=700)
    canvas.pack(fill="both")
    canvas.bind("<B1-Motion>", on_canvas_click)

    root.mainloop()
