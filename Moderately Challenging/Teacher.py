from Person import Person

class Teacher(Person):
    def __init__(self, name, address):
        super().__init__(name, address)
        self.__courses = []
        self.__number_of_courses = len(self.__courses)

    def get_number_of_courses(self):
        return self.__number_of_courses

    def add_course(self, course):
        if course in self.__courses:
            return False
        
        self.__courses.append(course)
        self.__number_of_courses = len(self.__courses)
        return True
        
    
    def remove_course(self, course):
        if course in self.__courses:
            self.__courses.remove(course)
            self.__number_of_courses = len(self.__courses)
            return True
        
        return False

    # toString()
    def __str__(self):
        return f"Teacher Name: {self._name}\nTeacher Address: {self._address}"
    