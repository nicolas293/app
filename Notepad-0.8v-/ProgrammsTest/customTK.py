import tkinter as tk

win = tk.Tk()
win.geometry('540x430')
win.resizable(0, 0)

def click():
    if label.winfo_ismapped():
        label.place_forget()
    else:
        label.place(y=40, x=5)

btn = tk.Button(win, text='click', command=click)
btn.place(y=10, x=5)

label = tk.Label(win, bg='red', height=20, width=30)



win.mainloop()