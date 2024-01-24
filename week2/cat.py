class Cat:
    # a constructor with 2 parameters
    def __init__(self, name, owner):
        self.name = name        # self.name is an attribute
        self.owner = owner      # self.owner is an attribute
    # a method without any parameter
    def says(self):
        print(f'{self.name} says meow!')

# create a Cat object
# kitty = Cat('Kitty', 'John')
# tom = Cat('Tom', 'Amy')

# access attribute of kitty
# print(kitty.name)
# print(kitty.owner)

# access method of kitty, tom
# kitty.says()
# tom.says()

# access attribute of tom to change
# tom.name = 'Tommy'
# tom.owner = 'Harry'
# tom.says()
# print(tom.owner)