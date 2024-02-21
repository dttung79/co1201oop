class Student:
    def __init__(self, id, name, gpa):
        self.__id = id
        self.__name = name
        self.__gpa = gpa
    
    def get_id(self):
        return self.__id
    
    def get_name(self):
        return self.__name
    
    def get_gpa(self):
        return self.__gpa
    
    def set_gpa(self, gpa):
        if gpa < 0 or gpa > 100:
            print("Invalid GPA")
        else:
            self.__gpa = gpa

    def show(self):
        print(f'ID: {self.__id}, Name: {self.__name}, GPA: {self.__gpa}')