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
        self.current = 0
    
    def create_widgets(self):
        lbl_books = Label(self.window, text='Books View')
        lbl_books.grid(row=0, column=2, sticky=W)

        btn_load = Button(self.window, text='Load', command=self.btn_load_clicked)
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

        btn_first = Button(self.window, text='|<', command=self.btn_first_clicked)
        btn_first.grid(row=7, column=0, sticky=W)

        btn_previous = Button(self.window, text='<<', command=self.btn_previous_clicked)
        btn_previous.grid(row=7, column=1, sticky=W)

        self.txt_id = Entry(self.window, width=5)
        self.txt_id.grid(row=7, column=2, sticky='NESW')
        self.txt_id.bind('<Return>', self.txt_id_entered)

        btn_next = Button(self.window, text='>>', command=self.btn_next_clicked)
        btn_next.grid(row=7, column=3, sticky=W)

        btn_last = Button(self.window, text='>|', command=self.btn_last_clicked)
        btn_last.grid(row=7, column=4, sticky=W)
    
    def btn_load_clicked(self):
        file_name = filedialog.askopenfilename()
        if file_name == '':
            msb.showinfo('Error', 'No file selected')
            return
        # load books to library
        self.library.load_books(file_name)
        # show the first book
        self.show_book(0)
    
    def show_book(self, index):
        try:
            id, title, author, price = self.library.get_book(index)
            self.set_text(self.txt_id, id)
            self.set_text(self.txt_author, author)
            self.set_text(self.txt_title, title)
            self.set_text(self.txt_price, price)
        except IndexError:
            msb.showinfo('Info', 'No book found. Please load books first.')
    
    def set_text(self, txt, text):
        txt.delete(0, END)
        txt.insert(0, text)

    def btn_next_clicked(self):
        if self.current == len(self.library.get_titles()) - 1:
            msb.showinfo('Info', 'This is the last book')
            return
        self.current += 1
        self.show_book(self.current)

    def btn_previous_clicked(self):
        if self.current == 0:
            msb.showinfo('Info', 'This is the first book')
            return
        self.current -= 1
        self.show_book(self.current)
    
    def btn_first_clicked(self):
        self.current = 0
        self.show_book(self.current)
    
    def btn_last_clicked(self):
        self.current = len(self.library.get_titles()) - 1
        self.show_book(self.current)

    def txt_id_entered(self, event):
        try:
            id = int(self.txt_id.get())
            index = self.library.search_id(id)
            if index is None:
                msb.showinfo('Info', 'Book not found')
                return
            self.current = index
            self.show_book(self.current)
        except ValueError:
            msb.showinfo('Error', 'Invalid ID. Must be an integer')

## Main starts here
program = BookViewGUI()
program.run()