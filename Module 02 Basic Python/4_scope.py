# global variable
balance=2000

def buy_things(item,price):
    # local scope variable
    # you can access global variable without using the global keyword
    drime_phone ='yphone'
    
    # if you want to modify a global variable, you have to use the global keyword 
    global balance
    print(f'previous balance value',balance)
    balance=balance-price
    print(f'balance after buying {item}',balance)
buy_things('phone',1000)