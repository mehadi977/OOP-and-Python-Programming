from abc import ABC,abstractmethod

class Project(ABC):
    def detaile(self):
        print('I am xyz project')
        
    @abstractmethod
    def security(self):
        pass
    
class App(Project):
    def detiels(self):
        print("im app project")
        
    def security(self):
        return super().security()
        
a=App()
a.detiels()
b=Project()
b.security()
