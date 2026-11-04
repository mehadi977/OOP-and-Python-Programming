""" 
What are Encapsulation and Access Modifiers? Explain with examples:

Encapsulation is use in a class for accesing the attribute or methd in object 

Public: accessable from anyware (name)
Private: no access use method for change or add (__name)
Protected: norma accessable form class and sub class (_name)

"""
# Exmple:
class Student:
    def __init__(self,name,roll,result):
        self.name=name #public
        self._roll=roll #protected
        self.__result=result #private
        
    def show_result(self):
        print(self.__result)
        
obj=Student('Khalid',11,79)

print(obj.name)
print(obj._roll)
print(obj.show_result())