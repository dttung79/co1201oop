from book import Book
from library import Library
from tkinter import *
from tkinter import messagebox as msb

class LibraryGUI:
    def __init__(self):
        try:
            self.library = Library()
        except FileNotFoundError:
            print('File not found')
            exit()
        self.window = self.create_window()
        self.create_widgets()
    
    def create_window(self):
        window = Tk()
        window.title('Library')
        window.geometry('500x300')
        return window
    
    def create_widgets(self):
        self.lbl_books = Label(self.window, text='Books')
        self.lbl_books.grid(row=0, column=0, sticky=W)

        self.lst_books = Listbox(self.window, width=30)
        self.lst_books.grid(row=1, column=0, rowspan=5, sticky=W)

        self.lbl_id = Label(self.window, text='ID')
        self.lbl_id.grid(row=1, column=2, sticky=E)

        self.txt_id = Entry(self.window, state='disabled', width=20)
        self.txt_id.grid(row=1, column=3, columnspan=3, sticky=W)

        self.lbl_title = Label(self.window, text='Title')
        self.lbl_title.grid(row=2, column=2, sticky=E)

        self.txt_title = Entry(self.window, width=20)
        self.txt_title.grid(row=2, column=3, columnspan=3, sticky=W)

        self.lbl_author = Label(self.window, text='Author')
        self.lbl_author.grid(row=3, column=2, sticky=E)

        self.txt_author = Entry(self.window, width=20)
        self.txt_author.grid(row=3, column=3, columnspan=3, sticky=W)

        self.lbl_price = Label(self.window, text='Price')
        self.lbl_price.grid(row=4, column=2, sticky=E)

        self.txt_price = Entry(self.window, width=20)
        self.txt_price.grid(row=4, column=3, columnspan=3, sticky=W)

        self.btn_add = Button(self.window, width=3, text='Add')
        self.btn_add.grid(row=5, column=3, sticky=W)

        self.btn_update = Button(self.window, width=3, text='Edit')
        self.btn_update.grid(row=5, column=4, sticky=W)

        self.btn_delete = Button(self.window, width=3, text='Del')
        self.btn_delete.grid(row=5, column=5, sticky=W)

        

    def run(self):
        self.window.mainloop()

####
program = LibraryGUI()
program.run()