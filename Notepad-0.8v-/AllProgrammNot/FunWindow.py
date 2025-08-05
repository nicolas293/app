from init import *
from time import strftime

class funWindowNew():
    def __init__(self):
        super().__init__()

    # рабочий стол функции

    def icoWindowNew(self):
        if self.windowDesk.winfo_ismapped():
            self.windowDesk.place_forget()
        else:
            self.windowDesk.place(y=40, x=5)    

    # рабочий стол функции

    # перемичение окан
    def start_move(self, event):
        global start_x, start_y
        start_x, start_y = event.x, event.y

    def move_widget(self, event):
        dx = event.x - start_x
        dy = event.y - start_y
        self.windowDesk.place(x=self.windowDesk.winfo_x() + dx, y=self.windowDesk.winfo_y() + dy)  
    # перемичение окан

    # клики по рабочему столу
    def clickDesck(self):
        if self.cal.winfo_ismapped():
            self.cal.place_forget()
        else:
            self.cal.place()

    def clickMenu(self):
        if self.menuLabel.winfo_ismapped():
            self.menuLabel.place_forget()
        else:
            self.menuLabel.place()    

    # клик по рабочему столу        

    # главное меню
    def menuWin(self):
        if self.menuLabel.winfo_ismapped():
            self.menuLabel.place_forget()    
        else:
            self.menuLabel.place(y=199, x=5)  
    # главное меню

    # календарь панели
    def CalPanell(self):
        if self.cal.winfo_ismapped():
            self.cal.place_forget()    
        else:
            self.cal.place(y=172, x=280)
    # календарь панели
                     
    # Время и дата
    def time(self):
        string = strftime('%H:%M:%S %p')
        self.maintime.config(text=string)
        self.maintime.after(1000, self.time)

    def grad_date(self):
        self.maintime.config(text = "Selected Date is: " + self.cal.get_date())    
    # Время и дата
