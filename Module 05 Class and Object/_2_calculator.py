""" HomeWork """
class Calculator:
    brand ='Casio MS999'
    # sum
    def add(self,num1,num2):
        ans=num1+num2
        return ans
    # deduct method
    def sub(self,num1,num2):
        return num1-num2
    # multiply method
    def mul(self,num1,num2):
        return num1*num2
    # divide method
    def div(self,num1,num2):
        return num1/num2

objct=Calculator()
print(objct.brand)
a=10
b=5
summ=objct.add(a,b)
subb=objct.sub(a,b)
mul=objct.mul(a,b)
div=objct.div(a,b)
print(summ,subb,mul,div)
    