class BankAccount:
    def __init__(self, acc_no, name, acc_bal):
        self.acc_no = acc_no
        self.name = name
        self.acc_bal = acc_bal
        
    def deposit(self, amount):
        self.acc_bal = self.acc_bal + amount
        return self.acc_bal
    
    def withdraw(self, amount):
        if amount < self.acc_bal:
            self.acc_bal = self.acc_bal - amount
            return self.acc_bal
        else:
            print("You don't have enough mate")
    
    def get_balance(self):
        print(self.acc_bal)
        
    def print_info(self):
        print(f'Account No: {self.acc_no}, Name: {self.name}, Account Balance: {self.acc_bal}')
    
person1 = BankAccount(1234,'Jeff',50000)

person1.withdraw(6000)
person1.deposit(100000)
person1.print_info()