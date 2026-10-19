class Shop:
    cart=[] #cart is a class attribute: shobgulor sathe share hoy
    def __init__(self,buyer):
        self.buyer=buyer
    
    def add_to_cart(self,item):
        self.cart.append(item)

me= Shop("Mehadi")
me.add_to_cart('shoes')
me.add_to_cart('phone')

she=Shop("Raicha")
she.add_to_cart('Watch')
she.add_to_cart('Chocolate')

print(me.cart)
print(she.cart)

        