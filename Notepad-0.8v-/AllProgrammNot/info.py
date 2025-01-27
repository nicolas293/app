import tkinter as tk

def newInfa():

    gut = tk.Toplevel()
    gut.title('Информация')
    gut.geometry('250x200')

    greeting = tk.Label(gut, text="Notepad_0.8v \n\n Nicolas nech", width=25, height=5)
    greeting.pack()

    def close_info():
        gut.destroy()

    button = tk.Button(gut, text='close', command=close_info)
    button.pack(side='top')

    gut.mainloop()