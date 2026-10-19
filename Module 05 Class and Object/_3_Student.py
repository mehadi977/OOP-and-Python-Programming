class Student:
    def __init__(self,name,roll,semister,result):
        self.name=name
        self.roll=roll
        self.semister=semister
        self.result=result

me=Student("Mehadi",842146,'5th',3.43)
tamim=Student("Tamim",83853,'7th',3.20)
print(me.name,me.roll,me.semister,me.result)
print(tamim.name,tamim.roll,tamim.semister,tamim.result)
        