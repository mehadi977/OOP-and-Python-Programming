# Ena Poribohon

class Company:
    def __init__(self,name,address):
        self.neme=name
        self.address=address
        self.bus=[]
        self.routes=[]
        self.drivers=[]
        self.counter=[]
        self.manager=[]
        self.supervisors=[]
        self.fare=[]

class Driver:
    def __init__(self,name,license,age):
        self.license=license
        self.name=name
        self.age=age
        
class Counter:
    def __init__(self):
        pass
    def purchase_a_ticket(self,start,destination):
        pass
    
class Passenger:
    pass
class Supervisor:
    pass

omuk=Driver()