from abc import ABC,abstractmethod
#abc=  abstract base class

class Animal(ABC):
    @abstractmethod #enforce all derived class to have eat mathod
    def eat(self):
        print('I need food')
    @abstractmethod
    def move(self):
        pass
    
class Monkey(Animal):
    def __init__(self,name):
        self.category='Monkey'
        self.name=name
        super().__init__()
    
    # shob child class ei eat rakha lagbe
    def eat(self):
        print('eat Banana')
        
    
        
layka=Monkey('lacka')
layka.eat()
