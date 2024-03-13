from tkinter import *
from tkinter import messagebox as msg
#### EVENT HANDLERS ####
def btn_OK_clicked():
    msg.showinfo('Info', 'OK button clicked')

#### CREATE WINDOW ####
window = Tk()
window.title('Hello GUI App')
window.geometry('300x200')

#### CREATE WIDGETS ####
lbl_message = Label(window, text='Hello World')
lbl_message.grid(row=0, column=0)

lbl_python = Label(window, text='Hello Python')
lbl_python.grid(row=1, column=1)

btn_OK = Button(window, text='OK', command=btn_OK_clicked)
btn_OK.grid(row=2, column=2)

#### START THE GUI ####
window.mainloop()