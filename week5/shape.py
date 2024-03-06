from abc import ABC, abstractmethod

# to define an abstract class, let it inherit from ABC
class Shape(ABC):
    def __init__(self, name):
        self._name = name       # protected attribute
        self._type = 'Shape'    # protected attribute
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        self._name = value

    @property
    def type(self):
        return self._type
    
    @abstractmethod
    def area(self):
        pass
    
    # return a string for printing Shape objects
    def __str__(self):
        return f'{self.type} {self.name}'