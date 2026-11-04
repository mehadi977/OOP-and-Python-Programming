class Phone:
    def __init__(self):
        print('this is Constructor')
    def __del__(self):
        print('this is distructor')
    def display(self):
        print('this is method')
  
   
        
p=Phone()
p.display()