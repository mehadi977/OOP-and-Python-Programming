class Phone:
    def __init__(self):
        print('this is Constructor')
    def __del__(self):
        print('this is distructor')
    def display(self):
        print('this is method')
        print(self)
  
def outside_func():
    print('Its outside function')
    
   
        
p=Phone()
p.display()
print(p)
Phone.outside_func=outside_func
print(Phone.__dict__.keys())