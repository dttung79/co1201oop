from book import Book
import csv
class Library:
    def __init__(self):
        self.__books = []
    
    def load_books(self, file_name):
        with open(file_name, 'r') as f:
            reader = csv.reader(f)
            # skip header
            next(reader)
            # scan each row
            for row in reader:
                id = int(row[0])
                title = row[1]
                author = row[2]
                price = float(row[3])
                b = Book(id, title, author, price)
                self.__books.append(b)

    def get_titles(self):
        return [b.title for b in self.__books] # list comprehension
    
    def get_book(self, index):
        # return self.__boks[index] => not safe, expose book's info to outside
        b = self.__books[index]
        # safe because we return a copy of book's info
        return b.id, b.title, b.author, b.price
    
    def update_book(self, index, title, author, price):
        b = self.__books[index]
        b.title = title
        b.author = author
        b.price = price
    
    def add_book(self, id, title, author, price):
        self.__books.append(Book(id, title, author, price))
        
    def delete_book(self, index):
        del self.__books[index]