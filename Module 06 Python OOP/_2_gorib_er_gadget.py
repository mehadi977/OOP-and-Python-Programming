class Laptop:
    def __init__(self,brand,price,color,memory):
        self.brand=brand
        self.price=price
        self.color=color
        self.memory=memory
        
    def run(self):
        return f'Running laptop:{self.brand}'
    
    def coading(self):
        return f'Learning python with phitron' 
    
class Phone:
    def __init__(self,brand,price,color,ram):
        self.brand=brand
        self.price=price
        self.color=color
        self.ram=ram
        
    def phone_call(self,number,text):
        return f'Sending sms to {number} with {text}'
    
    def run(self):
        return f'phone is running'

class Camera:
    def __init__(self,brand,price,pixel):
        self.brand=brand
        self.price=price
        self.pixel=pixel
    def run(self):
        pass
    def change_lens(self):
        pass
    
    
        