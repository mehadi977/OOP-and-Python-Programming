# Method overriging:
""" 
when a child class deifine a method in the same name as a method in parent class its call method overriding
"""

class Persion:
    def __init__(self,name,address):
        self.name=name
        self.address=address
    
    def doing(self):
        print(f'{self.name} are working ')
        
class Student(Persion):
    def __init__(self, name, address):
        super().__init__(name, address)
        
# method overriding
    def doing(self):
        return super().doing()
        # print(f'{self.name} are reading book')
    
p=Persion('khalid','dhaka')
s=Student('shanto','dhaka')
p.doing()
s.doing()