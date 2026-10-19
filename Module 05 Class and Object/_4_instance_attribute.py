class Shop:
    shopping_mall='Dhaka te'
    def __init__(self,name):
        self.neme=name
        self.cart=[] #cart is an instance attribute: object alada alada hobe
        
    def add_to_cart(self,item):
        self.cart.append(item)
        
me=Shop("Mehadi")
me.add_to_cart('Phone')
me.add_to_cart('Shirt')
me.add_to_cart('Mouse')

she=Shop("Raicha")
she.add_to_cart('Watch')
she.add_to_cart('Dress')
she.add_to_cart('book')


print(me.neme,me.cart)
print(she.neme,she.cart)        