class Bank:
    def __init__(self,name,balance):
        self.name=name
        self.__balance=balance
        
    def getBalance(self):
        print(self.__balance)
        
abc=Bank("ABC",1000)
# print(abc.balance)
# abc.__balance=0
# print(abc.__balance)
abc.getBalance()

print(Bank.__dict__.keys())