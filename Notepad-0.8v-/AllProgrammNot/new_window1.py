import tkinter as tk
from tkinter import scrolledtext

def new_window1_size_text(parent_window, text_widget):
    if not text_widget:
        raise ValueError("text_widget is required")
        
    my_w = tk.Toplevel(parent_window)
    my_w.title('Size-текст-0.5v')
    my_w.geometry("400x300")

    # Создаем фрейм для лучшей организации элементов
    frame = tk.Frame(my_w)
    frame.pack(pady=20)

    # Начальные настройки шрифта
    current_font = {
       'family': 'Arial',
       'size': 12,
       'weight': 'normal',
       'slant': 'roman'
    }

    def update_font():
        text_widget.configure(font=(current_font['family'], 
                            current_font['size'],
                            current_font['weight'],
                            current_font['slant']))
        
    def change_size(delta):
        current_font['size'] = max(8, min(72, current_font['size'] + delta))
        size_label.config(text=f"Размер шрифта: {current_font['size']}")
        update_font()

    def on_scale_change(value):
        current_font['size'] = int(float(value))
        size_label.config(text=f"Размер шрифта: {current_font['size']}")
        update_font()
    # Кнопки изменения размера
    tk.Button(frame, text='+', command=lambda: change_size(2), width=5).grid(row=0, column=0, padx=5)
    tk.Button(frame, text='-', command=lambda: change_size(-2), width=5).grid(row=0, column=1, padx=5)
    # Метка с текущим размером
    size_label = tk.Label(frame, text=f"Размер шрифта: {current_font['size']}")
    size_label.grid(row=1, column=0, columnspan=2, pady=10)
    # Слайдер для размера шрифта
    scale = tk.Scale(frame, from_=8, to=72, orient='horizontal', 
                   command=on_scale_change, length=200)
    scale.set(current_font['size'])
    scale.grid(row=2, column=0, columnspan=2, pady=10)
    # Стили текста
    style_frame = tk.Frame(frame)
    style_frame.grid(row=3, column=0, columnspan=2, pady=10)
   
    def toggle_bold():
        current_font['weight'] = 'normal' if current_font['weight'] == 'bold' else 'bold'
        update_font()

    def toggle_italic():
        current_font['slant'] = 'roman' if current_font['slant'] == 'italic' else 'italic'
        update_font()

    tk.Button(style_frame, text='Жирный', command=toggle_bold).pack(side='left', padx=5)
    tk.Button(style_frame, text='Курсив', command=toggle_italic).pack(side='left', padx=5)