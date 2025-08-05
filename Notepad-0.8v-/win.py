import tkinter as tk
from init import *
from NotepadNew import *

class AppNotepad(tk.Tk, funWindowNew):
    def __init__(self):
        super().__init__()

        self.canvas = tk.Button(self, activeforeground=None, text='', height=430, width=540, command=lambda:(self.clickDesck(), self.clickMenu()))
        self.canvas.pack(fill='both')
        
        # рабочий стол
        
        self.windowDesk = tk.Frame(self, bg='#bcbbc2', bd=3, height=200, width=200, relief='ridge')
        
        self.iconsWindow = tk.Button(self, text='new window', bg='#bcbbc2', bd=3, relief='ridge', command=self.icoWindowNew)
        self.iconsWindow.place(y=5, x=5)

        self.windowPanell = tk.Frame(self.windowDesk, height=30, width=187, bg="#49484b", bd=3, relief='ridge')
        self.windowPanell.place(y=5, x=5)

        self.textWin = tk.Text(self.windowDesk, relief='ridge', bd=3, height=9, width=22)
        self.textWin.place(y=38, x=5)

        self.windowEixt = tk.Button(self.windowDesk, text='X', relief='ridge', bd=3, command=self.icoWindowNew)
        self.windowEixt.place(y=6, x=170)
        
        # рабочий стол

        # главное меню
        self.label = tk.Label(self, bg='#bcbbc2', relief='ridge', bd=3, foreground='white', height=3, width=75)
        self.label.place(y=370, x=5)

        self.btn = tk.Button(self, text='Menu', bg='#aaaba9', fg='#17181a', height=2, width=6, command=self.menuWin)
        self.btn.place(y=375, x=10)
        # главное меню

        # меню панели 
        self.menuLabel = tk.Label(self, bg='#89898a', relief='ridge', bd=3, height=10, width=20)

        self.virtualkey = tk.Button(self.menuLabel, bg='#aaaba9', fg='#17181a', text='Клавиотура', command=lambda:(VirtualKeyboard(root=self), Application()))
        self.virtualkey.place(y=40, x=5)
        
        self.calculate = tk.Button(self.menuLabel, bg='#aaaba9', fg='#17181a', text='Триугольник', command=lambda:(my_calculate_window(parent_window=self)))
        self.calculate.place(y=75, x=5)

        self.menuNotepad = tk.Button(self.menuLabel, bg='#aaaba9', fg='#17181a', text='Notepad', command=Notepad)
        self.menuNotepad.place(y=10, x=5)
        # меню панели

        # Время и дата
        self.maintime = tk.Button(background=None, foreground=None, bg='#aaaba9', fg='#17181a', width=11, height=2, command=self.CalPanell)
        self.maintime.place(y=375, x=440)

        self.cal = Calendar(self, selectmode = 'day', year = 2025, month = 5, day = 22)
        
        self.time()
        # Время и дата

        # перемичение окан
        self.windowDesk.bind('<Button-1>', self.start_move)
        self.windowDesk.bind('<B1-Motion>', self.move_widget)

        self.windowPanell.bind('<Button-1>', self.start_move)
        self.windowPanell.bind('<B1-Motion>', self.move_widget)
        # перемичение окан

        # контекстное меню
        self.menu = tk.Menu(self, tearoff=0)
        self.menu.add_cascade(label='Terminal', command=lambda:(create_terminal_window(), execute_command()))
        
        self.bind("<Button-3>", self.menuDesctop)

    def menuDesctop(self, event):
        self.menu.tk_popup(event.x_root, event.y_root)
    # контекстное меню
   
if __name__ == '__main__':
    app = AppNotepad()
    app.title('window')
    app.resizable(0, 0)
    app.geometry('540x430')
    app.mainloop()