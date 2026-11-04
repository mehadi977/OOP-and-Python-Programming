# Write what are getter and setter with proper examples
""" 
1.getter:
getter is a method to  use for visit a private and protected attribute

2.setter:
setter is a method to use access or modify the value of an attribute

"""
# Exmple:
class Student:
    def __init__(self, marks):
        self.__marks = marks

    @property
    def marks(self):          # Getter
        return self.__marks

    @marks.setter
    def marks(self, value):   # Setter
        if value >= 0:
            self.__marks = value


s = Student(80)

print(s.marks)  # Getter

s.marks = 95    # Setter

print(s.marks)