import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
import random

win = tk.Tk()
win.title('Игра в кости')
win.geometry('300x150')

def play():
	random_number = random.randint(1,6)
	number.config(text=f'Выпало {random_number}')
	if random_number == 6: 
	   showinfo('Поздравляю вы выиграли')


number = ttk.Label(win, text='')
number.pack(pady=10)

play = ttk.Button(win,text='Play', command=play)
play.pack(padx=50)

win.mainloop()