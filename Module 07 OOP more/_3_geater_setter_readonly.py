#read only -->you can not set the value.value can not be changed
#getter --> get a value of property through a method. Most of the time, you will get the value of a private attribute.
# setter --> set a value of a property through a method. Most of the time you will set the value of a private proporty.
class Person:
    def __init__(self,name,age,money):
        self._name=name
        self._age=age
        self.__money=money
    #getter without any setter is readonly atribute
    @property
    def show_age(self):
        return self._age
    # getter 
    @property
    def show_money(self):
        return self.__money
    @property #getter -> no changeable
    def salary(self):
        return self.__money
    
    @salary.setter #setter -> changeable
    def salary(self,value):
        if(value<0):
            return 'salary can not be negative'
        self.__money+=value
        print('selary added') 
    
smasu=Person('kupa',25,30000)
print(smasu._name)
print(smasu._age)
# print(smasu.__money)
# print(smasu.show_age()) @proparty use kole method call kora jai na method ta attribute hoye jai. tokhon attribute er moto kore call korte hoy

print(smasu.show_age)
# print(smasu.show_money()) 
print(smasu.show_money) 
# smasu.salary(9)
smasu.salary=990
print(smasu.salary)

