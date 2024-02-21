# from file name import class name
from student import Student
class ClassRoom:
    def __init__(self, name):
        self.__name = name
        self.__students = []
    
    def get_name(self):
        return self.__name

    def add_student(self, student):
        self.__students.append(student)
        print(f'{student.get_name()} has been added to the class.')
    
    def remove_student(self, sid):
        for s in self.__students:
            if s.get_id() == sid:
                self.__students.remove(s)
                print(f'{s.get_name()} has been removed from the class.')
                return
        print(f'Student with ID {sid} not found.')
    
    def show(self):
        print(f'Class name: {self.__name}')
        print(f'All students in the class:')
        for s in self.__students:
            s.show()
        
        print(f'Average GPA: {self.avg_gpa()}')
    
    def show_best(self):
        if len(self.__students) == 0:
            print('No students in the class.')
            return
        
        best = self.__students[0]
        for s in self.__students:
            if s.get_gpa() > best.get_gpa():
                best = s
        
        return best
    
    def avg_gpa(self):
        if len(self.__students) == 0:
            print('No students in the class.')
            return
        
        sum_gpa = 0
        for s in self.__students:
            sum_gpa += s.get_gpa()
        return sum_gpa / len(self.__students)