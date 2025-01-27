import tkinter as tk
from tkinter import Label

def newPomaq():

    gut = tk.Toplevel()
    gut.title('Помощь')
    gut.geometry('250x200')
    gut.resizable(False, False)

    def open_link():
        import webbrowser
        webbrowser.open("https://t.me/nic293nechepaev")

    link_label = Label(gut, text="Кликните здесь, что бы открыть Телеграмм!! \n\n nicolas", fg="blue", cursor="hand2", width=25, height=5)
    link_label.pack(fill='both')

    link_label.bind("<Button-1>", lambda e: open_link())

    gut.mainloop()