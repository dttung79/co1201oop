from pet import Pet
class Dog(Pet):
    def __init__(self, name, age, owner):
        super().__init__(name, age, owner)
    
    def woof(self):
        print('Woof woof!')