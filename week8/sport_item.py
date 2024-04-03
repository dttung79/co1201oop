class SportItem:
    def __init__(self, id, nam, brand, price): # branch
        self.__id = id
        self.__name = nam
        self.__brand = brand
        self.__price = price
    
    # provide getter for all attributes
    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @property
    def brand(self):
        return self.__brand

    @property
    def price(self):
        return self.__price    
    
    # provide setter for name, brand and price attributes
    @name.setter
    def name(self, value):
        if value == '':
            raise ValueError('Name cannot be empty')
        self.__name = value
    
    @brand.setter
    def brand(self, value):
        if value == '':
            raise ValueError('Brand cannot be empty')
        self.__brand = value
    
    @price.setter
    def price(self, value):
        try:
            value = float(value)
            if value <= 0:
                raise ValueError('Price must be positive')
            self.__price = value
        except ValueError:
            raise ValueError('Price must be number')