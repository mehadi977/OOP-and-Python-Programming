""" Homework """
class Pen:
    product="Pen"
    def __init__(self,company,color,price):
        self.company=company
        self.color=color
        self.price=price
        
my_pen=Pen('My pen Metador','Black',5)
her_pen=Pen('Her pen GoodLuck','Red',10)
print(my_pen.company,my_pen.color,my_pen.price)
print(her_pen.company,her_pen.color,her_pen.price)

        