from Person import Person

class Student(Person):
    def __init__(self, name, address):
        super().__init__(name, address)
        self.__course = []
        self.__grades = []

    def get_average_grade(self):
        sum = 0
        for i in self.__course:
            sum += self.__grades[self.__course.index(i)][i]
        
        return sum / len(self.__course)

    def add_course_grade(self, course, grade):
        self.__course.append(course)
        self.__grades.append({course: grade})

    def print_grades(self):
        for i in self.__course:
            print(f"{i}: {self.__grades[self.__course.index(i)][i]}")
    
    def __str__(self):
        return f"Student Name: {self._name}\nStudent Address: {self._address}"