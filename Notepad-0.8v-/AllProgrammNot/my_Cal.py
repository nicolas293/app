import tkinter as tk
from tkinter import Button, Label
from tkcalendar import Calendar

def mycal():
    cali = tk.Toplevel()
    cali.title('Календарь')
    cali.geometry('400x400')

    cal = Calendar(cali, selectmode = 'day', year = 2025, month = 5, day = 22)
    cal.pack(pady = 20)

    def grad_date():
        date.config(text = "Selected Date is: " + cal.get_date())

    Button(cali, text = "Get Date",
            command = grad_date).pack(pady = 20)
 
    date = Label(cali, text = "")
    date.pack(pady = 20)

    cali.mainloop()