class Phone:
    manufactured='China'
    
    def __init__(self,owner,brand,price,):
        self.owner=owner
        self.brand=brand
        self.price=price
        
my_phone=Phone('jani na','Samsung',15000)
print(my_phone.owner,my_phone.brand,my_phone.price)
her_phone=Phone('tao jani na','Tecno',20000)
print(her_phone.owner,her_phone.brand,her_phone.price)

