from tkinter import *
from tkinter import messagebox as msg

### EVENT HANDLERS ###
def btn_add_clicked():
    operator('+')

def btn_sub_clicked():
    operator('-')

def operator(op):
    a = int(txt_a.get()) # get content of entry txt_a
    b = int(txt_b.get()) # get content of entry txt_b
    if op == '+':
        c = a + b
    elif op == '-':
        c = a - b
    #lbl_result.config(text=c) # set text of label lbl_result
    lbl_result['text'] = str(c)
    
### CREATE WINDOW ###
window = Tk()
window.title('Arithmetic Operators')
window.geometry('300x200')

### CREATE WIDGETS ###
lbl_a = Label(window, text='a = ')
lbl_a.grid(row=0, column=0)

txt_a = Entry(window, width=10)
txt_a.grid(row=0, column=1)

lbl_b = Label(window, text='b = ')
lbl_b.grid(row=1, column=0)

txt_b = Entry(window, width=10)
txt_b.grid(row=1, column=1)

lbl_c = Label(window, text='c = ')
lbl_c.grid(row=2, column=0)

lbl_result = Label(window, text='')
lbl_result.grid(row=2, column=1, sticky=W)

btn_add = Button(window, text='Add', command=btn_add_clicked)
btn_add.grid(row=3, column=1, sticky=W)

btn_sub = Button(window, text='Subtract', command=btn_sub_clicked)
btn_sub.grid(row=4, column=1, sticky=W)

### START THE GUI ###
window.mainloop()