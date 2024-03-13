class Product:
    def __init__(self, name, price, quantity):
        self.__name = name
        self.__price = price
        self.__quantity = quantity
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        if value == '':
            raise ValueError('Name cannot be empty')
        self.__name = value

    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError('Price cannot be negative')
        self.__price = value

    @property
    def quantity(self):
        return self.__quantity
    
    @quantity.setter
    def quantity(self, value):
        if value < 0:
            raise ValueError('Quantity cannot be negative')
        self.__quantity = value
    
    def show(self):
        print(f'Name: {self.__name}, price: ${self.__price}, quantity: {self.__quantity}')