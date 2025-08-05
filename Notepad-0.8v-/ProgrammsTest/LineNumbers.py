import tkinter as tk
import tkinter as ttk
from init import *
from tkinter.scrolledtext import Frame, ScrolledText

root = tk.Tk()
root.resizable(False, False)
root.geometry("540x430")

text_frame = Frame(root)
text_frame.pack(side="left", fill="both")

label = Label()
label.pack(anchor=None, fill='both')

line_numbers_text = tk.Text(text_frame, width=3)
line_numbers_text.pack(side='left', fill='y')

main_text = ScrolledText(text_frame)
main_text.pack(side='left', fill='both')

line_numbers_text.config(state='disabled', bg="lightgray")

def update_line_numbers(event=None):
    lines = main_text.get("1.0", "end-1c").count("\n") + 1

    line_numbers_text.config(state="normal")
    line_numbers_text.delete("1.0", tk.END)
    line_numbers_text.insert(tk.END, "\n".join(str(i) for i in range(1, lines + 1)))
    line_numbers_text.config(state="disabled")

    line_numbers_text.yview_moveto(main_text.yview()[0])

def ColorsText():
    color = ch.askcolor()
    if color[1] is not None:
        main_text.configure(fg=color[1])

def ColorFon():
    color = ch.askcolor()
    if color[1] is not None:
        main_text.configure(bg=color[1])

def my_popup(e):
    my_menu.tk_popup(e.x_root, e.y_root)

def pasteText():
    main_text.event_generate("<<Paste>>") 

def copyText():
    main_text.event_generate("<<Copy>>")

main_text.bind("<<Modified>>", update_line_numbers)
main_text.bind("<KeyRelease>", update_line_numbers)
root.bind("<Button-3>", my_popup)

my_menu = tk.Menu(tearoff=0)
my_menu.add_command(label='paste text', command=pasteText)
my_menu.add_command(label='copy text', command=copyText)

edit = tk.Menu(tearoff=0)
edit.add_command(label='color text', command=ColorsText)
edit.add_command(label='color fon', command=ColorFon)

file = tk.Menu(tearoff=0)
file.add_command(label="Open File")
file.add_command(label='File Save')
file.add_separator()
file.add_command(label='quit', command=quit)

menu = tk.Menu(tearoff=0)
menu.add_cascade(label='File', menu = file)
menu.add_cascade(label='Edit', menu = edit)
menu.add_cascade(label='Info')
root.config(menu=menu)

root.mainloop()