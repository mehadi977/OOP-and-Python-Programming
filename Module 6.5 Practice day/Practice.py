class Product:
   
    def __init__(self,product_name,price,quantity):
        self.product_name=product_name
        self.price=price
        self.quantity=quantity
        self.product={'product_name': self.product_name,'price':self.price,'quantity':self.quantity}        

class Shop:
    def __init__(self):
        self.all_product=[]
       
    def add_product(self,product_name,price,quantity):    
        item= Product(product_name,price,quantity) 
        self.all_product.append(item.product)
        
    def buy_product(self,product_name,quantity):
        for item in self.all_product:
            if(item['product_name']==product_name and item['quantity']>=quantity):
                item['quantity']-=quantity
                print('Congratulation You can buy this product')
                return
            
        print('Sorry! Not avalivle')
                
    
    
shp=Shop()

shp.add_product('am',30,5)
shp.add_product('banana',15,50)
shp.add_product('apple',80,100)
shp.add_product('orange',40,200)
shp.buy_product('am',4)

# print(shp)