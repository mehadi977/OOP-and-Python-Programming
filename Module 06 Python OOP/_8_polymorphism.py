# poly --> many(multiple)
# morph -->shape
 
class Animal:
    def __init__(self,name):
        self.name=name
        
    def make_sound(self):
        print('animal making sound')
        
        
class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)
        
    # def make_sound(self):
    #     return super().make_sound()
    def make_sound(self):
        print('meow meow')
        
class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)
        
    def make_sound(self):
        print('gheu gheu')
        
class Goat(Animal):
    def __init__(self, name):
        super().__init__(name)
        
    def make_sound(self):
        print('bea bea')
        

        
don = Cat('don')
don.make_sound()

kutta= Dog('kutta')
print(kutta.make_sound())

mess=Goat('L M')
mess.make_sound()

rono=Goat('ronoda')
animls=[don,kutta,mess,rono]
for animl in animls:
    print(animl.make_sound())
