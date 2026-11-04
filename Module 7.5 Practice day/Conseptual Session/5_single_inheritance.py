class Animal:
    def __init__(self,name):
        self.name=name
    def eat(self):
        print(self.name,' can eat')

class Cat(Animal):
    # def __init__(self,name):
    #     self.name=name
    def __init__(self, name):
        super().__init__(name)
        
    def sound(self):
        print('mew')
        
        
class Dog(Animal):
    def __init__(self, name):
       super().__init__(name)
        
    def sound(self):
        print('Bark')
        
cat=Cat('cat')
cat.eat()
print(cat.name)
cat.sound()
dog=Dog('dog')
dog.eat()
print(dog.name)
dog.sound()