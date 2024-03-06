from account import Account

class NormalAccount(Account):
    def __init__(self, id, name):
        super().__init__(id, name)
    
    def withdraw(self, amount):
        if amount <= 0:
            print("Amount must be greater than 0")
            return
        if amount > self.balance:
            print("Insufficient balance")
            return
        self._balance -= amount
        print(f"Withdrawal successful. Current balance: {self.balance}")
    
    def __str__(self):
        return super().__str__() + ", Type: Normal"