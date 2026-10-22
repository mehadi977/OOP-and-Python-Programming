# Encapsulation --> hide details
# access modifier: public,private,protected
class Bank:
    def __init__(self,holder_name,initial_deposit):
        self.holder_name=holder_name #Public
        
        # self.balance=balance
        self.__balance= initial_deposit #private:class er baire theke access kora jabe na (__)use for private
        
        self._brance='Dhaka' #Protected
        
        
    def deposit(self,amount):
        self.__balance+=amount
        
    def get_balance(self):
        return self.__balance
    
    def withdraw(self,amount):
        if amount<self.__balance:
            self.__balance-=amount
            return amount
        else:
            return f'taka nai'
    
        
mehadi=Bank('Mehadi',5000)
print(mehadi.holder_name)
# mehadi.balance=0
# print(mehadi.__balance)
mehadi.deposit(3000)
# print(mehadi.get_balance())
mehadi.holder_name='Notun nam'
print(mehadi.holder_name)
print(mehadi._brance)

# jor kore access kora 
print(dir(mehadi))
print(mehadi._Bank__balance) 