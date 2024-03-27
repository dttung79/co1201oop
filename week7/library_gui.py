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

        self.load_titles()
    
    def create_window(self):
        window = Tk()
        window.title('Library')
        window.geometry('500x300')
        return window
    
    def create_widgets(self):
        self.lbl_books = Label(self.window, text='Books')
        self.lbl_books.grid(row=0, column=0, sticky=W)

        self.lst_books = Listbox(self.window, width=30, exportselection=False)
        self.lst_books.grid(row=1, column=0, rowspan=5, sticky=W)
        self.lst_books.bind('<<ListboxSelect>>', self.lst_books_selected)

        self.lbl_id = Label(self.window, text='ID')
        self.lbl_id.grid(row=1, column=2, sticky=E)

        self.txt_id = Entry(self.window, width=20)
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

        self.btn_add = Button(self.window, width=3, text='Add', command=self.btn_add_clicked)
        self.btn_add.grid(row=5, column=3, sticky=W)

        self.btn_update = Button(self.window, width=3, text='Edit', command=self.btn_edit_clicked)
        self.btn_update.grid(row=5, column=4, sticky=W)

        self.btn_delete = Button(self.window, width=3, text='Del', command=self.btn_delete_clicked)
        self.btn_delete.grid(row=5, column=5, sticky=W)
    
    def load_titles(self):
        titles = self.library.get_titles()
        # clear listbox
        self.lst_books.delete(0, END)
        # insert titles
        for t in titles:
            self.lst_books.insert(END, t)
        
    def lst_books_selected(self, event):
        index = self.lst_books.curselection()[0]
        id, title, author, price = self.library.get_book(index)
        
        self.txt_id.delete(0, END)
        self.txt_id.insert(0, id)

        self.txt_title.delete(0, END)
        self.txt_title.insert(0, title)

        self.txt_author.delete(0, END)
        self.txt_author.insert(0, author)

        self.txt_price.delete(0, END)
        self.txt_price.insert(0, price)

    def btn_add_clicked(self):
        # get book's info from textboxes
        id = int(self.txt_id.get())
        title = self.txt_title.get()
        author = self.txt_author.get()
        price = float(self.txt_price.get())
        
        self.library.add_book(id, title, author, price) # add to library
        self.lst_books.insert(END, title)               # add to listbox

        msb.showinfo('Add book', 'Book added succesfully')

    def btn_edit_clicked(self):
        # get book's info from textboxes
        title = self.txt_title.get()
        author = self.txt_author.get()
        price = float(self.txt_price.get())
        # get selected index
        index = self.lst_books.curselection()[0]
        # update library
        self.library.update_book(index, title, author, price)
        # update listbox
        self.lst_books.delete(index)
        self.lst_books.insert(index, title)

        msb.showinfo('Update book', 'Book updated succesfully')
    
    def btn_delete_clicked(self):
        # get selected index
        index = self.lst_books.curselection()[0]
        # delete from library
        self.library.delete_book(index)
        # delete from listbox
        self.lst_books.delete(index)

        msb.showinfo('Delete book', 'Book deleted successfully')

    def run(self):
        self.window.mainloop()

####
program = LibraryGUI()
program.run()