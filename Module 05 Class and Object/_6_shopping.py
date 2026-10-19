class Shopping:
    def __init__(self,name):
        self.name=name
        self.cart=[]
        
    def add_to_cart(self,item,price,quantity):
        product={'item':item,'price':price,'quantity':quantity}
        self.cart.append(product)
    
    def checkout(self,amount):
        total=0
        for item in self.cart:
            # print(item)
            total+=item['price']*item['quantity']
        print('total: ',total)
        if(amount<total):
            print(f'Plese provide: {total-amount} more')
        else:
            extra=amount-total
            print(f'here is your item and extra money {extra}')
            
    # HomeWork
    def remove_from_cart(self,item_name):
        for product in self.cart:
            if(product['item']==item_name):
                self.cart.remove(product)
                print(f'item {item_name} remove from cart')
                return
        print(f'item {item_name} is not in cart')
            
        
            
            

        

obj= Shopping('Mehadi')
obj.add_to_cart('alu',60,10)
obj.add_to_cart('dim',12,20)
obj.add_to_cart('begun',50,5)
# print(obj.cart)
obj.checkout(2000)
obj.remove_from_cart('alu')
print(obj.cart)
obj.remove_from_cart('dal')