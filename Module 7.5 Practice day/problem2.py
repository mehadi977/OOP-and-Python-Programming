# Find out which of these players is older using the operator overloading.

class Person:
    def __init__(self, name, age, height, weight) -> None:
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

class Cricketer(Person):
    def __init__(self, name, age, height, weight) -> None:
        super().__init__(name, age, height, weight)
        
    def __gt__(self, other):
        return self.age> other.age

sakib = Cricketer('Sakib', 38, 68, 91)
musfiq = Cricketer('Rahim', 36, 68, 88)
kamal = Cricketer('Kamal', 39, 68, 94)
jack = Cricketer('Jack', 38, 68, 91)
kalam = Cricketer('Kalam', 37, 68, 95)

player=[sakib,musfiq,kamal,jack,kalam]

oldest=player[0]
for all in player:
    if(all>oldest):
        oldest=all
        
print(oldest.name," ",oldest.age)
    