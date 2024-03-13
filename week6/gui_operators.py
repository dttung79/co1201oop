from tkinter import *
from tkinter import messagebox as msg
class GUIOperators:
    def __init__(self):
        ### CREATE WINDOW ###
        self.window = Tk()
        self.window.title('Arithmetic Operators')
        self.window.geometry('300x200')

        ### CREATE WIDGETS ###
        self.lbl_a = Label(self.window, text='a = ')
        self.lbl_a.grid(row=0, column=0)

        self.txt_a = Entry(self.window, width=10)
        self.txt_a.grid(row=0, column=1)

        self.lbl_b = Label(self.window, text='b = ')
        self.lbl_b.grid(row=1, column=0)

        self.txt_b = Entry(self.window, width=10)
        self.txt_b.grid(row=1, column=1)

        self.lbl_c = Label(self.window, text='c = ')
        self.lbl_c.grid(row=2, column=0)

        self.lbl_result = Label(self.window, text='')
        self.lbl_result.grid(row=2, column=1, sticky=W)

        self.btn_add = Button(self.window, text='Add', command=self.btn_add_clicked)
        self.btn_add.grid(row=3, column=1, sticky=W)

        self.btn_sub = Button(self.window, text='Subtract', command=self.btn_sub_clicked)
        self.btn_sub.grid(row=4, column=1, sticky=W)

    def btn_add_clicked(self):
        self.operator('+')

    def btn_sub_clicked(self):
        self.perator('-')

    def operator(self, op):
        a = int(self.txt_a.get()) # get content of entry txt_a
        b = int(self.txt_b.get()) # get content of entry txt_b
        if op == '+':
            c = a + b
        elif op == '-':
            c = a - b
        #lbl_result.config(text=c) # set text of label lbl_result
        self.lbl_result['text'] = str(c)
    
    def run(self):
        self.window.mainloop()

### START THE GUI ###
program = GUIOperators()
program.run()