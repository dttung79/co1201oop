from tkinter import *
from tkinter import messagebox as msg

class GUIWindow:
    def __init__(self):
        #### CREATE WINDOW ####
        self.window = Tk()
        self.window.title('Hello GUI App')
        self.window.geometry('300x200')

        #### CREATE WIDGETS ####
        self.lbl_message = Label(self.window, text='Hello World')
        self.lbl_message.grid(row=0, column=0)

        self.lbl_python = Label(self.window, text='Hello Python')
        self.lbl_python.grid(row=1, column=1)

        self.btn_OK = Button(self.window, text='OK', command=self.btn_OK_clicked)
        self.btn_OK.grid(row=2, column=2)
    
    def btn_OK_clicked(self):
        msg.showinfo('Info', 'OK button clicked')
    
    def run(self):
        self.window.mainloop()

#### run the program ####
program = GUIWindow()
program.run()
