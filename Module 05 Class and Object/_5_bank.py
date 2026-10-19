class Bank:
    def __init__(self,balance):
        self.balance=balance
        self.min_withdraw=100
        self.max_withdraw=10000
        
    def get_balance(self):
        return self.balance
    
    def diposit(self,amount):
        if(amount>0 and amount<10001):
            self.balance+=amount
            
    def withdraw(self,amount):
        if(amount<self.min_withdraw):
            print (f' {self.min_withdraw} er kom hobe na re fokir')
        elif( amount>self.max_withdraw):
            print (f'{self.max_withdraw} er besi withdraw korte parba na')
        else:
            self.balance-=amount
            print (f'Here is your money{amount}')
            print(f'your balance after withdraw {self.balance}')

my_acc=Bank(1000)
print(my_acc.balance)
my_acc.withdraw(59)
my_acc.withdraw(100)
my_acc.diposit(-1)
print(my_acc.balance)
my_acc.withdraw(3999999)
my_acc.diposit(500)
print(my_acc.balance)
my_acc.withdraw(200)

dbbl=Bank(5000)
dbbl.diposit(200)
dbbl.diposit(200)
print(dbbl.balance)

