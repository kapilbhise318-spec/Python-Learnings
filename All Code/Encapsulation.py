class BankAccount:
    def __init__(self,name,balance):
        self.name=name
        self.__balance=balance      #Private class

    def deposit (self,amount):
        self.__balance += amount

    def getbalance(self):
        return self.__balance
    
acc=BankAccount("Kapil",50000)
acc.deposit(100000)
print(acc.getbalance())
# print(acc.__balance)  

    
