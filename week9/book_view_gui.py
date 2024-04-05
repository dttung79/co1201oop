from base_gui import BaseGUI
from tkinter import *
from tkinter import messagebox as msb
from book import Book
from library import Library
from tkinter import filedialog

class BookViewGUI(BaseGUI):
    def __init__(self):
        super().__init__('Book View', '300x300')
        self.library = Library()
        self.create_widgets()
    
    def create_widgets(self):
        lbl_books = Label(self.window, text='Books View')
        lbl_books.grid(row=0, column=2, sticky=W)

        btn_load = Button(self.window, text='Load')
        btn_load.grid(row=0, column=3, columnspan=2, sticky=E)

        lbl_title = Label(self.window, text='Title')
        lbl_title.grid(row=1, column=0, sticky=W)

        self.txt_title = Entry(self.window, width=30)
        self.txt_title.grid(row=2, column=0, columnspan=5, sticky=W)

        lbl_author = Label(self.window, text='Author')
        lbl_author.grid(row=3, column=0, sticky=W)

        self.txt_author = Entry(self.window, width=30)
        self.txt_author.grid(row=4, column=0, columnspan=5, sticky=W)

        lbl_price = Label(self.window, text='Price')
        lbl_price.grid(row=5, column=0, sticky=W)

        self.txt_price = Entry(self.window, width=30)
        self.txt_price.grid(row=6, column=0, columnspan=5, sticky=W)

        btn_first = Button(self.window, text='|<')
        btn_first.grid(row=7, column=0, sticky=W)

        btn_previous = Button(self.window, text='<<')
        btn_previous.grid(row=7, column=1, sticky=W)

        self.txt_id = Entry(self.window, width=5)
        self.txt_id.grid(row=7, column=2, sticky='NESW')

        btn_next = Button(self.window, text='>>')
        btn_next.grid(row=7, column=3, sticky=W)

        btn_last = Button(self.window, text='>|')
        btn_last.grid(row=7, column=4, sticky=W)

### Main starts here
program = BookViewGUI()
program.run()