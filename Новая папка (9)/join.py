from tkinter import *
from tkinter import messagebox
import random

def no():
	messagebox.showinfo(' ', 'А я так и знал')
	quit()

def motionMouse(event):
	btnn.place(x=random.randint(0,500), y=random.randint(0, 500))


root = Tk()
root.geometry('900x600')
root.title('Опрос программистов')
root.resizable(width = False, height = False)
root ['bg'] = 'green'

label = Label(root, text='Ты программист?', font= 'Arial 20 bold', bg= 'silver').pack()
btnn = Button(root, text= 'Нет', font= 'Arial 20 bold')
btnn.place(x=170, y=100)
btnn.bind('<Enter>', motionMouse)

btmy = Button(root, text= 'Да', font= 'Arial 20 bold', command=no).place(x=350, y=100)

root.mainloop()