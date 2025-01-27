import tkinter as tk

def button_click(event):
    button = event.widget
    text = button['text']
    print(f'Нажмите на кнопку: {text}')

root = tk.Tk()
root.title('Эранная клавиатура')

aplhabet = 'abcdefghijklmnopqrstuvwxyz'
row = 1
column = 0

for letter in aplhabet:
    button = tk.Button(root, text=letter, width=5, height=2)
    button.grid(row=row, column=column)
    # button.bind('', button_click)
    column += 2
    if column > 10:
        column = 0
        row += 1

button_space = tk.Button(root, text='Пробел', width=20, height=2)
button_space.grid(row=row+1, column=2, columnspan=5)
# button_space.bind('', button_click)



