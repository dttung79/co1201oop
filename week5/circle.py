from shape import Shape

class Circle(Shape):
    def __init__(self, name, radius):
        super().__init__(name)  # initialize the parent class with name attribute
        self.__radius = radius  # private attribute
        self._type = 'Circle'   # protected attribute from Shape

    @property
    def radius(self):
        return self.__radius
    
    @radius.setter
    def radius(self, value):
        self.__radius = value

    # override the abstract method from the parent class
    def area(self):
        return 3.14 * self.__radius ** 2
    
    # override the __str__ method from the parent class
    def __str__(self):
        return super().__str__() + f', radius: {self.__radius}'