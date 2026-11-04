""" 
What is inheritance:
inheritance is a core concept in object oriented programing
super class --> sub class
"""
# Exmpl:
class Animal:
    def __init__(self,name):
        self.name=name
    def eat(self):
        print(f'{self.name} are eating')
        
class cat(Animal):
    def __init__(self, name):
        super().__init__(name)
    def sound(self):
        print(f'{self.name} says maw maw')

ct=cat('catt')
ct.sound()
ct.eat()