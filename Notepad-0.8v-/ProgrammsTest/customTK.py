import customtkinter as ct

ct.set_appearance_mode("system")
ct.set_default_color_theme("dark-blue")

win = ct.CTk()
win.resizable(False, False)
win.geometry("540x430")

castom = 0



def menuG(event=None):
    eventar = ct.CTkButton(master=win, text='File', height=40, corner_radius=10)
    eventar.pack(side='bottom', pady=10)
    
    eventar = ct.CTkButton(master=win, text='Edit', height=40, corner_radius=10)
    eventar.pack(side='bottom', ipady=10, pady=10)

    eventar = ct.CTkButton(master=win, text='Quit', corner_radius=10, command=quit)
    eventar.pack(side='bottom', pady=10)
    
    button.configure(state='disabled')
        
menu = ct.CTkFrame(master=win, fg_color='red', border_color='green', height=50)
menu.pack(side='bottom', fill='both')

# menu1 = ct.CTkOptionMenu(master=menu)
# menu1.pack(fill='both')

button = ct.CTkButton(master=menu, text='МЕНЮ', command=menuG)
button.pack(side='left')





win.mainloop()