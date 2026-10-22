class Book:
    def __init__(self,name):
        self.name=name
        
    def read(self):
        raise NotImplementedError
        
class Physics(Book):
    def __init__(self, name,lab):
        self.lab=lab
        super().__init__(name)
    def read(self):
        print('reading vector')
        
topon =Physics('topon',True)

print(issubclass(Physics,Book))#subclass kina ck
print(isinstance(topon,Physics))#instance kina ck
print(isinstance(topon,Book))

topon.read()