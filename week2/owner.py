from cat import Cat

class Owner:
    def __init__(self, name, pet):
        self.name = name
        self.pet = pet
    
    def show_pet(self):
        print(f'I\'m {self.name}, my pet is {self.pet.name}.')

kitty = Cat('Kitty', 'John')
john = Owner('John', kitty)

john.show_pet()