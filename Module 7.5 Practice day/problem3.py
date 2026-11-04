""" 
Write down 4 differences between the class method and static method with proper examples.


class method------                    
1.decorator: uses @class method                    
1.first parameter: takes cls as fst parameter  
3.Accessing cls attrubut:can access cls attribute using cls    
4. Purpose: Used to access or modify class-level data.

static method------
1.decorator:  uses @staticmethod
2.first parameter:  does not requred self or cls
3.Can access class attributes explicitly using the class name.
4. Purpose: Used to perform independent tasks related to the class.
"""
# Exmple:

class Student: 
    school="ABC school"
    @classmethod
    def show_scl(cls):
        print(cls.school)
    @staticmethod
    def add(a,b):
        print(a+b)
        
a=Student()
a.show_scl()
a.add(3,5)