from Student import Student
from Teacher import Teacher

import random

Harry = Student("Harry Potter", "4 Privet Drive, Little")

print(Harry.__str__())
Harry.add_course_grade("Astronomy", random.randrange(40) + 60)
Harry.add_course_grade("Charms", random.randrange(40) + 60)
Harry.add_course_grade("Dark Arts", random.randrange(40) + 60)
Harry.add_course_grade("Defence Against Dark Arts", random.randrange(40) + 60)
Harry.print_grades()

print(f"Average grade: {Harry.get_average_grade()}")

print("------------------------------------------------------------")

snape = Teacher("Severus Snape", "Shrieking Shack, Hogsmeade, Highlands, Scotland")

print(snape.__str__())
snape.add_course("Potion")
print(snape.add_course("Potion")) # print false
snape.add_course("Dark Arts")
print(f"{snape.get_name()} teaches {snape.get_number_of_courses()} {'course' if snape.get_number_of_courses() <= 1 else 'courses'}")
snape.remove_course("Dark Arts")
print(snape.remove_course("Dark Arts")) # print false
print(f"{snape.get_name()} teaches {snape.get_number_of_courses()} {'course' if snape.get_number_of_courses() <= 1 else 'courses'}")
