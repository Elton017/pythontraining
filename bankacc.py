class BankAcc:
    def __init__(self, accno, accho, bal):
        self.accno = accno
        self.accho = accho
        self.bal = bal
    
    def deposit(self, amount):
        self.bal += amount
        return self.bal
    
    def withdraw(self, amount):
        if self.bal >= amount:
            self.bal -= amount
        else:
            print("not enough")
        return self.bal
    
    def get_bal(self):
        return self.bal
    
    def __str__(self):
        return f'Account Number: {self.accno}, Account Holder: {self.accho}, Balance: {self.bal}'
        
class CheckingAcc(BankAcc):
    def __init__(self, accno, accho, bal):
        super().__init__(accno, accho, bal)
    
    def withdraw(self, amount):
        fee = float(amount / 100)
        if self.bal >= amount + fee:
            self.bal -= amount + fee
            return self.bal
        else:
            print('2 poor')

class SavingsAcc(BankAcc):
    def __init__(self,accno, accho, bal, interest):
        super().__init__(accno, accho, bal)
        self.interest = interest
    
    def add_interest(self):
        self.bal += self.bal * (self.interest / 100)
        return self.bal
    
x = BankAcc('1', 'jeff', 100000)
y = CheckingAcc('1', 'jeff', 100000)
z = SavingsAcc('1', 'jeff', 100000, 2.5)
print(y.withdraw(100))
print(z.add_interest())