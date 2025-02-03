import tkinter as tk
from __init__ import *

win = tk.Tk()
win.geometry('560x450')
win.iconbitmap(default="icons/notepad_icon1.ico")
win.title('Notepad-0.8v')

win['borderwidth'] = 2
win['relief'] = 'sunken'

is_modified = False
original_title = 'Notepad_0.8v'
setup_window_closing(win, is_modified)

line_numbers_widget = LineNumberWidget(win)
line_numbers = line_numbers_widget.main_text

text_widget = line_numbers
status_bar = StatusBar(line_numbers, text_widget)   


# Функции Notepad-0.8v
def size_text():
    new_window1_size_text(win, line_numbers)      

def my_calculate_win():
    my_calculate_window(win)

is_modified = False
original_title = 'Notepad_0.8v' 
setup_window_closing(win, is_modified)

def update_title():
   if is_modified:
       win.title(f'*{original_title}')
   else:
       win.title(original_title)

def on_text_change(event=None):
   global is_modified
   is_modified = True
   update_title()
   
line_numbers.bind('<<Modified>>', on_text_change)

def new_file():
    line_numbers.delete(1.0, tk.END)

def OpenFile(event): # Функция открытей фаела
    global is_modified
    file_path = fd.askopenfilename()
    if file_path:
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
                line_numbers.delete('1.0', 'end')
                line_numbers.insert('1.0', content)
            is_modified = False
            update_title()
        except Exception as e:
            messagebox.showerror("Error", str(e))

def SaveFile(event): # Функция сохранение фаела
    global is_modified
    file_path = fd.asksaveasfilename(defaultextension=".txt",
                                   filetypes=[("Text files", "*.txt"),
                                            ("All files", "*.*")])
    if file_path:
       try:
            with open(file_path, 'w', encoding='utf-8') as file:
               content = line_numbers.get('1.0', 'end-1c')
               file.write(content)
            is_modified = False
            update_title()
       except Exception as e:
           messagebox.showerror("Error", str(e))

def colorPicer():
    color = ch.askcolor()
    if color[1] is not None:
        line_numbers.configure(fg=color[1])

def clearTextInputQ():
    line_numbers.delete("1.0", "end")

def colorPicerFons():
    color = ch.askcolor()
    if color[1] is not None:
        line_numbers.configure(bg=color[1])
    
def my_popup(e): 
   my_menu.tk_popup(e.x_root, e.y_root)

def on_click(event):
    print("Клик")

def my_copy():
    line_numbers.event_generate("<<Copy>>")

def my_paste():
    line_numbers.event_generate("<<Paste>>")
     
def Quit():
    MsgBox = messagebox.askquestion("Выход из Программы: Notepad-0.8v", "Ты диствительно хочешь выйти?")
    if MsgBox == 'yes':
        win.destroy()
# Функции Notepad-0.8v

# icons menu
iconsOpen = tk.PhotoImage(file="icons/openicon.png")
saveicon = tk.PhotoImage(file="icons/saveicon.png")
newfile = tk.PhotoImage(file="icons/newfile.png")
quiticon = tk.PhotoImage(file="icons/quiticon.png")
# icons menu

win.bind("<Button-1>", on_click)
win.bind("<Button-3>", my_popup)

# быстрее клавиши
win.bind("<Control-Key-o>", OpenFile)
win.bind("<Control-Key-s>", SaveFile)
# быстрее клавиши

my_menu = Menu(win, background='#66c1d0', tearoff=0)
my_menu.add_command(label='Open File', command=OpenFile)
my_menu.add_command(label='Save File', command=SaveFile)
my_menu.add_separator()
my_menu.add_command(label='Copy Text', command=my_copy)
my_menu.add_command(label='Paste Text', command=my_paste)
my_menu.add_separator()
my_menu.add_command(label='Цыфровый часы', command=myTeme)
my_menu.add_command(label='Календарь', command=mycal)
my_menu.add_separator()
my_menu.add_command(label='Выбор Цвета', command=myStytsColor)
my_menu.add_separator()
my_menu.add_command(label='Color-Текст', command=colorPicer)
my_menu.add_command(label='Color-фон', command=colorPicerFons)
my_menu.add_command(label='Clear', command=clearTextInputQ)
my_menu.add_separator()
my_menu.add_command(label='Canvas-Рисовалка', command=new_window)
my_menu.add_command(label='Font-Текст', command=size_text)
my_menu.add_separator()
my_menu.add_command(label='Quit File', command=Quit)

edit = Menu(win, background='#66c1d0', tearoff=0)
edit.add_command(label='Color-текст', command=colorPicer)
edit.add_command(label='Color-фон', command=colorPicerFons)
edit.add_command(label='Text Edit')
edit.add_separator()
edit.add_command(label='Canvas-Рисовалка', command=new_window)
edit.add_command(label='Font Size', command=size_text)
edit.add_separator()
edit.add_command(label='Canvas-угольники', command=my_calculate_win)
edit.add_separator()
edit.add_command(label='чётчик слов', command=my_counter)

file = Menu(win, background='#66c1d0', tearoff=0)
file.add_command(label='New File', command=new_file, image=newfile, compound='left')
file.add_separator()
file.add_command(label='Open File', command=OpenFile, image=iconsOpen, compound='left', accelerator='Ctrl+O')
file.add_command(label='Save File', command=SaveFile, image=saveicon, compound='left', accelerator='Ctrl+S')
file.add_separator()
file.add_command(label='Выбор Цвета', command=myStytsColor)
file.add_separator()
file.add_command(label='Цыфровый часы', command=myTeme)
file.add_command(label='Календарь', command=mycal)
file.add_separator()
file.add_command(label='Auto-закрытие', command=lambda: windowsOpenWin(win))
file.add_separator()
file.add_command(label='Quit File', command=Quit, image=quiticon, compound='left')

editVersions = Menu(win, background='#66c1d0', tearoff=0)
editVersions.add_command(label='Помощь', command=newPomaq)
editVersions.add_command(label='Информация о версии', command=newInfa)

menu = Menu(win, tearoff=0)
menu.add_cascade(label='File', menu=file)
menu.add_cascade(label='Edit', menu=edit)
menu.add_cascade(label='Version', menu=editVersions)
win.config(menu=menu)

win.mainloop()