from sport_item import SportItem
from sport_store import SportStore
from tkinter import *
from tkinter import messagebox as msb
from tkinter import filedialog

class SportGUI:
    def __init__(self):
        self.store = SportStore()
        self.window = self.create_window('Sport Store', '550x300')
        self.create_widgets()
    
    def create_window(self, title, dimension):
        window = Tk()
        window.title(title)
        window.geometry(dimension)
        return window
    
    def create_widgets(self):
        lbl_items = Label(self.window, text='All Items')
        lbl_items.grid(row=0, column=0, sticky=W)

        self.lst_items = Listbox(self.window, width=30, height=10)
        self.lst_items.grid(row=1, column=0, columnspan=2, rowspan=5, sticky=W)

        lbl_id = Label(self.window, text='ID')
        lbl_id.grid(row=1, column=2, sticky=W)
        self.txt_id = Entry(self.window, width=20)
        self.txt_id.grid(row=1, column=3, columnspan=3, sticky=W)

        lbl_name = Label(self.window, text='Name')
        lbl_name.grid(row=2, column=2, sticky=W)
        self.txt_name = Entry(self.window, width=20)
        self.txt_name.grid(row=2, column=3, columnspan=3, sticky=W)

        lbl_brand = Label(self.window, text='Brand')
        lbl_brand.grid(row=3, column=2, sticky=W)
        self.txt_brand = Entry(self.window, width=20)
        self.txt_brand.grid(row=3, column=3, columnspan=3, sticky=W)

        lbl_price = Label(self.window, text='Price')
        lbl_price.grid(row=4, column=2, sticky=W)
        self.txt_price = Entry(self.window, width=20)
        self.txt_price.grid(row=4, column=3, columnspan=3, sticky=W)

        btn_add = Button(self.window, text='Add')
        btn_add.grid(row=5, column=3, sticky=W)

        btn_update = Button(self.window, text='Update')
        btn_update.grid(row=5, column=4, sticky=W)

        btn_delete = Button(self.window, text='Delete')
        btn_delete.grid(row=5, column=5, sticky=W)

        btn_load = Button(self.window, text='Load', command=self.btn_load_clicked)
        btn_load.grid(row=6, column=0, sticky=W)

        btn_save = Button(self.window, text='Save', command=self.btn_save_clicked)
        btn_save.grid(row=6, column=1, sticky=E)

        btn_exit = Button(self.window, text='Exit', command=self.window.quit)
        btn_exit.grid(row=6, column=5, sticky=E)

    def btn_load_clicked(self):
        file_name = filedialog.askopenfilename()
        if file_name == '':
            msb.showerror('Error', 'No file selected')
            return
        # load items to store
        self.store.load_items(file_name)
        # fill list box with items' names
        self.fill_listbox()
    
    def btn_save_clicked(self):
        file_name = filedialog.asksaveasfilename()
        if file_name == '':
            msb.showerror('Error', 'No file selected')
            return
        # save items to file
        self.store.save_items(file_name)
    
    def fill_listbox(self):
        names = self.store.get_names()
        for name in names:
            self.lst_items.insert(END, name)

    def run(self):
        self.window.mainloop()

### Main starts here
if __name__ == '__main__':
    app = SportGUI()
    app.run()