import tkinter as tk
from tkinter import Label
from time import strftime

def myTeme():
    tqme = tk.Toplevel()
    tqme.title('Цифровые Часы')

    lable = Label(tqme, font=('aerial', 30), background='black', foreground='white')

    def time():
        string = strftime('%H:%M:%S %p')
        lable.config(text=string)
        lable.after(1000, time)

    lable.pack(anchor='center')
    time()

    tqme.mainloop()