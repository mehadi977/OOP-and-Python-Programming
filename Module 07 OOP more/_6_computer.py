# inheritance is a relation
# composition has a relation

class CPU:
    def __init__(self,core):
        self.core=core

class RAM:
    def __init__(self,size):
        self.size=size
        
class SSD:
    def __init__(self,capacity):
        self.capacity=capacity
        
class GPU:
    def __init__(self,brand):
        self.brand=brand
        
# its compositon
# computer has a cpu
# computer has a ram
# computer has a ssd
# computer has a gpu

class Computer:
    def __init__(self,cpu_core,ram_size,ssd_capacity,gpu_brand):
        self.cpu=CPU(cpu_core)
        self.ram=RAM(ram_size)
        self.ssd=SSD(ssd_capacity)
        self.gpu=GPU(gpu_brand)
        
        
mac=Computer(8,16,512,'RTX')

        