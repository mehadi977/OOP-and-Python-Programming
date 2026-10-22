# base class, parent class, common attribute+functionality class

# derived class class,child class, uncommon attribute+functionality

# base class:
class Gadget: 
    def __init__(self,brand,price,color,origin):
        self.brand=brand
        self.price=price
        self.color=color
        self.origin=origin
    
    def run(self):
        return f'Running laptop{self.br}'
        

 
class Laptop:
    def __init__(self,memory,ssd):
        self.memory=memory
        self.ssd=ssd
    
    def coading(self):
        return f'Learning python with phitron' 
    
class Phone(Gadget):
    def __init__(self,brand,price,color,origin,dual_sim):
        self.dual_sim=dual_sim
        super().__init__(brand,price,color,origin)
        
    def phone_call(self,number,text):
        return f'Sending sms to {number} with {text}'
    def __repr__(self):
        return f'phone:{self.dual_sim}'


class Camera:
    def __init__(self,pixel):
        self.pixel=pixel

    def change_lens(self):
        pass
    
    
# inheritance
# my_phone=Phone(True)
my_phone=Phone('Realme',12000,'Black','China',True)
# my_phone.brand('Realme')
print(my_phone)
print(my_phone.brand)