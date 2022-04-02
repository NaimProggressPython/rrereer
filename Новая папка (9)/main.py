from tkinter import *

root = Tk()
root.title('Realese')
root.wm_attributes('-alpha',0.8)
root.geometry('400x400')

frame = Frame(root, bg='red')
frame.place(relx=0.15, rely=0.15, relwidth=0.7, relheight=0.7)

canvas = Canvas(root, height=300, width=250)
canvas.pack()

title = Label(frame, text='Введите пароль', bg='blue', font=40)
btn = Button(frame, text='Нажми', bg='Blue')
btn.pack()

loginInput = Entry(frame, bg='white')
loginInput.pack()

passField = Entry(frame, bg='white', show='*')
passField.pack()



root.mainloop()