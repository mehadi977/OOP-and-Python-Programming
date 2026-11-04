class Persion:
    def __init__(self,name,age,height,weight):
        self.name=name
        self.age=age
        self.height=height
        self.weight=weight
    
    # sub class e eat name kono method nai tai eat call korle eta print hobe
    def eat(self):
        print('vat, mach,mangsho , dim')
        
    def gym(self):
        raise NotImplementedError

class Cricketer(Persion):
    def __init__(self, name, age, height, weight,team):
        self.team=team
        super().__init__(name, age, height, weight)
        
    # super class eo eki name e method ache kintu kintu method call korle sub class er ta call hobe super class er ta avoid korbe 
    # This is Method override
    def eat(self):
        print("Vasitable")
    def gym(self):
        print('Gym kore')
        
    # + sign operator overload
    def __add__(self, other):
        return self.age+other.age
    # * sign operator overload
    def __mul__(self, other):
        return self.weight*other.weight
    # len overload
    def __len__(self):
        return self.height
    # >operator overload
    def __gt__(self, other):
        return self.age>other.age
    
        
        
shanto=Cricketer('Shanto',25,68,70,'BD')
ridoy=Cricketer('ridoy',24,63,65,'BD')


shanto.eat()
shanto.gym()

# plus(+) sign overload
print(45+63)
print('sakib'+'Rakib')
print([12,13]+[2,6,22,5])
print(shanto + ridoy)
print(shanto*ridoy)
print(len(shanto))
print(shanto>ridoy)
