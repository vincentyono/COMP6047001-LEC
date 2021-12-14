from Person import Person

class Teacher(Person):
    def __init__(self, name, address):
        super().__init__(name, address)
        self.__courses = []
        self.__number_of_courses = len(self.__courses)

    def get_number_of_courses(self):
        return self.__number_of_courses

    def add_course(self, course):
        is_exist = False
        for i in self.__courses:
            if i == course:
                is_exist = True
        
        if is_exist:
            return False
        else:
            self.__courses.append(course)
            self.__number_of_courses = len(self.__courses)
    
    def remove_course(self, course):
        is_exist = False
        for i in self.__courses:
            if i == course:
                is_exist = True

        if is_exist:
            self.__courses.remove(course)
            self.__number_of_courses = len(self.__courses)
        else:
            return False

    # toString()
    def __str__(self):
        return f"Teacher Name: {self._name}\nTeacher Address: {self._address}"
    