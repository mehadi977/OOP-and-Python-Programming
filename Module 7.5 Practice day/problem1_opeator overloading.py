# Write what is meant by operator overloading and method overriding with examples.

""" 
Operater overloading->:
-- operator overloading is a technique that allows python operator(+,-,*./) to perfome specific operation on object of a class

"""
# Example:
class Calculator:
    def __init__(self,val):
        self.val=val
    def __add__(self, other):
        return self.val+other.val
    def __sub__(self, other):
        return self.val-other.val
    def __mul__(self, other):
        return self.val*other.val
    
    
a= Calculator(4)
b=Calculator(2)
print(a+b)
print(a-b)
print(a*b)