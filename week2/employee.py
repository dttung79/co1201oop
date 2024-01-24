class Employee:
    def __init__(self, name, salary, years):
        self.name = name
        self.salary = salary
        self.years = years
    
    def show(self):
        print(f'Employee: {self.name}, salary: ${self.salary}, years of experience: {self.years}')

john = Employee('John', 50000, 5)
john.show()

john.salary = 60000
john.show()