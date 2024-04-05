from tkinter import *
from abc import ABC, abstractmethod

class BaseGUI(ABC):
    def __init__(self, title, dimension):
        self.window = self.create_window(title, dimension)
        self.create_widgets()
    
    def create_window(self, title, dimension):
        window = Tk()
        window.title(title)
        window.geometry(dimension)
        return window
    
    @abstractmethod
    def create_widgets(self):
        pass

    def run(self):
        self.window.mainloop()