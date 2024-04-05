class Book:
    def __init__(self, id, title, author, price):
        if not isinstance(id, int) or id < 0:
            raise ValueError('ID must be integer and non-negative')
        if title == '':
            raise ValueError('Title cannot be empty')
        if author == '':
            raise ValueError('Author cannot be empty')
        if not (isinstance(price, float) or isinstance(price, int)) or price <= 0:
            raise ValueError('Price must be number and positive')
        self.__id = id
        self.__title = title
        self.__author = author
        self.__price = price
    
    @property
    def id(self):
        return self.__id
    @property
    def title(self):
        return self.__title
    
    @title.setter
    def title(self, title):
        if title == '':
            raise ValueError('Title cannot be empty')
        self.__title = title
    
    @property
    def author(self):
        return self.__author
    
    @author.setter
    def author(self, author):
        if author == '':
            raise ValueError('Author cannot be empty')
        self.__author = author

    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self, price):
        if not (isinstance(price, float) or isinstance(price, int)) or price <= 0:
            raise ValueError('Price must be number and positive')
        self.__price = price