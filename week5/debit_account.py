from account import Account

class DebitAccount(Account):
    def __init__(self, id, name, limit):
        super().__init__(id, name)
        self.__limit = limit
    
    def withdraw(self, amount):
        if amount > self.balance + self.__limit:
            print("Insufficient balance")
            return
        
        if amount <= 0:
            print("Amount must be greater than 0")
            return
        
        self._balance -= amount
        print(f"Withdrawal successful. Current balance: {self.balance}")
    
    def __str__(self):
        return super().__str__() + f", Type: Debit, Limit: -${self.__limit}"