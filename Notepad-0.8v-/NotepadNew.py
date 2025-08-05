import tkinter as tk
from init import *

class Notepad(tk.Toplevel):
    def __init__(self):
        super().__init__()

        self['borderwidth'] = 2
        self['relief'] = 'sunken'

        is_modified = False
        self.original_title = 'Notepad_0.8v'
        setup_window_closing(self, is_modified)

        self.line_numbers_widget = LineNumberWidget(self)
        self.line_numbers = self.line_numbers_widget.main_text

        self.text_widget = self.line_numbers
        self.status_bar = StatusBar(self.line_numbers, self.text_widget)  

        self.line_numbers.bind('<<Modified>>', self.on_text_change)    

        self.iconsOpen = tk.PhotoImage(file="icons/openicon.png")
        self.saveicon = tk.PhotoImage(file="icons/saveicon.png")
        self.newfile = tk.PhotoImage(file="icons/newfile.png")
        self.quiticon = tk.PhotoImage(file="icons/quiticon.png")

        self.bind("<Button-1>", self.on_click)
        self.bind("<Button-3>", self.my_popup)

        # быстрее клавиши
        self.bind("<Control-Key-o>", self.OpenFile)
        self.bind("<Control-Key-s>", self.SaveFile)
        # быстрее клавиши

        self.my_menu = Menu(self, background='#66c1d0', tearoff=0)
        self.my_menu.add_command(label='Open File', command=self.OpenFile)
        self.my_menu.add_command(label='Save File', command=self.SaveFile)
        self.my_menu.add_separator()
        self.my_menu.add_command(label='Copy Text', command=self.my_copy)
        self.my_menu.add_command(label='Paste Text', command=self.my_paste)
        self.my_menu.add_separator()
        self.my_menu.add_command(label='Цыфровый часы', command=myTeme)
        self.my_menu.add_command(label='Календарь', command=mycal)
        self.my_menu.add_separator()
        self.my_menu.add_command(label='Выбор Цвета', command=myStytsColor)
        self.my_menu.add_separator()
        self.my_menu.add_command(label='Color-Текст', command=self.colorPicer)
        self.my_menu.add_command(label='Color-фон', command=self.colorPicerFons)
        self.my_menu.add_command(label='Clear', command=self.clearTextInputQ)
        self.my_menu.add_separator()
        self.my_menu.add_command(label='Canvas-Рисовалка', command=new_window)
        self.my_menu.add_command(label='Font-Текст', command=self.size_text)
        self.my_menu.add_separator()
        self.my_menu.add_command(label='Quit File', command=self.Quit)

        self.edit = Menu(self, background='#66c1d0', tearoff=0)
        self.edit.add_command(label='Color-текст', command=self.colorPicer)
        self.edit.add_command(label='Color-фон', command=self.colorPicerFons)
        self.edit.add_command(label='Terminal', command=lambda:(create_terminal_window(), execute_command()))
        self.edit.add_separator()
        self.edit.add_command(label='Canvas-Рисовалка', command=new_window)
        self.edit.add_command(label='Font Size', command=self.size_text)
        self.edit.add_command(label='Экраная Клавиотура', command=lambda:(VirtualKeyboard(root=self), Application()))
        self.edit.add_separator()
        self.edit.add_command(label='Canvas-угольники', command=self.my_calculate_win)
        self.edit.add_separator()
        self.edit.add_command(label='чётчик слов', command=my_counter)

        self.file = Menu(self, background='#66c1d0', tearoff=0)
        self.file.add_command(label='New File', command=self.new_file, image=self.newfile, compound='left')
        self.file.add_separator()
        self.file.add_command(label='Open File', command=self.OpenFile, image=self.iconsOpen, compound='left', accelerator='Ctrl+O')
        self.file.add_command(label='Save File', command=self.SaveFile, image=self.saveicon, compound='left', accelerator='Ctrl+S')
        self.file.add_separator()
        self.file.add_command(label='Выбор Цвета', command=myStytsColor)
        self.file.add_separator()
        self.file.add_command(label='Цыфровый часы', command=myTeme)
        self.file.add_command(label='Календарь', command=mycal)
        self.file.add_separator()
        self.file.add_command(label='Auto-закрытие', command=lambda: windowsOpenWin(self))
        self.file.add_separator()
        self.file.add_command(label='Quit File', command=self.Quit, image=self.quiticon, compound='left')

        self.editVersions = Menu(self, background='#66c1d0', tearoff=0)
        self.editVersions.add_command(label='Помощь', command=newPomaq)
        self.editVersions.add_command(label='Информация о версии', command=newInfa)

        self.menu = Menu(self, tearoff=0)
        self.menu.add_cascade(label='File', menu=self.file)
        self.menu.add_cascade(label='Edit', menu=self.edit)
        self.menu.add_cascade(label='Version', menu=self.editVersions)
        self.config(menu=self.menu)


    def size_text(self):
        new_window1_size_text(self, self.line_numbers)      

    def my_calculate_win(self):
        my_calculate_window(win)

    def update_title(self):
        if is_modified:
            self.title(f'*{self.original_title}')
        else:
            self.title(self.original_title)

    def on_text_change(self, event=None):
        global is_modified
        is_modified = True
        self.update_title()

    def new_file(self):
        self.line_numbers.delete(1.0, tk.END)

    def OpenFile(self, event): # Функция открытей фаела
        global is_modified
        file_path = fd.askopenfilename()
        if file_path:
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    content = file.read()
                    self.line_numbers.delete('1.0', 'end')
                    self.line_numbers.insert('1.0', content)
                is_modified = False
                self.update_title()
            except Exception as e:
                messagebox.showerror("Error", str(e))

    def SaveFile(self, event): # Функция сохранение фаела
        global is_modified
        file_path = fd.asksaveasfilename(defaultextension=".txt",
                                    filetypes=[("Text files", "*.txt"),
                                                ("All files", "*.*")])
        if file_path:
            try:
                with open(file_path, 'w', encoding='utf-8') as file:
                    content = self.line_numbers.get('1.0', 'end-1c')
                    file.write(content)
                    is_modified = False
                    self.update_title()
            except Exception as e:
                messagebox.showerror("Error", str(e))

    def colorPicer(self):
        color = ch.askcolor()
        if color[1] is not None:
            self.line_numbers.configure(fg=color[1])

    def clearTextInputQ(self):
        self.line_numbers.delete("1.0", "end")

    def colorPicerFons(self):
        color = ch.askcolor()
        if color[1] is not None:
            self.line_numbers.configure(bg=color[1])

    def my_popup(self, e): 
        self.my_menu.tk_popup(e.x_root, e.y_root)

    def on_click(self, event):
        print("Клик")

    def my_copy(self):
        self.line_numbers.event_generate("<<Copy>>")

    def my_paste(self):
        self.line_numbers.event_generate("<<Paste>>")
        
    def Quit(self):
        MsgBox = messagebox.askquestion("Выход из Программы: Notepad-0.8v", "Ты диствительно хочешь выйти?")
        if MsgBox == 'yes':
            self.destroy()


if __name__ == '__main__':
    win = Notepad(tk.Toplevel)
    win.transient()
    win.geometry('560x450')
    # win.overrideredirect(True)
    win.iconbitmap(default="icons/notepad_icon1.ico")
    win.title('Notepad-0.8v')
    # win.mainloop()