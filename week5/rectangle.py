from shape import Shape

class Rectangle(Shape):
    def __init__(self, name, width, height):
        super().__init__(name)
        self._width = width
        self._height = height
        self._type = 'Rectangle'
    
    @property
    def width(self):
        return self._width
    
    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height
    
    @height.setter
    def height(self, value):
        self._height = value

    
    def area(self):
        return self._width * self._height
    
    def __str__(self):
        return super().__str__() + f', size: {self._width} x {self._height}'