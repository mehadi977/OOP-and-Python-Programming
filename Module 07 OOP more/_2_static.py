# static attribute(class attribute)
# static method @staticmethod
# class method @classmethod
# defferences between static method and class method
class Shopping:
    cart=[] #class attribute #static attribute
    origin='China'
    def __init__(self,name,location):
        self.name=name  #instance attribute
        self.location='dhaka'
        
    def purchase(self,item,price,amount):
        remining=amount-price
        print(f'buying: {item} for price: {price} and remainging: {remining} ')
    @classmethod   
    def hudai_dekhi(self,item):
        print('kinbo na sudhu dekhte ashci')
    @staticmethod        
    def multiply(a,b):
        print(a*b)
        
Shopping.purchase('a','bb',45,34)

basundhara=Shopping('basundhara','Dhaka')
basundhara.purchase('shirt',500,2)
# Shopping.hudai_dekhi('jjjj') #hobe na karon function er age @classmethod use korte hobe
basundhara.hudai_dekhi('juta')
Shopping.hudai_dekhi('kjkjkj') #after use @classmethod

Shopping.multiply(4,5) #static method


basundhara.multiply(2,6)