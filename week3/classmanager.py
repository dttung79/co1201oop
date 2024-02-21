from student import Student
from classroom import ClassRoom

class ClassManager:
    def __init__(self):
        name = input('Enter the name of the class: ')
        self.__room = ClassRoom(name)
    
    def run(self):
        while True:
            self.print_menu()
            choice = int(input('Enter your choice: '))
            if choice == 1:
                self.add_student()
            elif choice == 2:
                self.remove_student()
            elif choice == 3:
                self.show_students()
            elif choice == 4:
                self.show_best()
            elif choice == 5:
                break
            else:
                print('Invalid choice. Try again.')
    
    def print_menu(self):
        print(f'Class Manager for {self.__room.get_name()}')
        print('1. Add student')
        print('2. Remove student')
        print('3. Show students')
        print('4. Show best student')
        print('5. Quit')
    
    def add_student(self):
        id = int(input('ID: '))     # enter id
        name = input('Name: ')      # enter name
        gpa = float(input('GPA: ')) # enter gpa
        s = Student(id, name, gpa)  # create a student object
        self.__room.add_student(s)  # add the student to the classroom
    
    def remove_student(self):
        id = int(input('ID: '))     # enter id
        self.__room.remove_student(id)
    
    def show_students(self):
        self.__room.show()
    
    def show_best(self):
        best = self.__room.show_best()
        if best:
            print('Best student:')
            best.show()


### main program
program = ClassManager()
program.run()