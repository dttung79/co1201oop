class Account:
    def __init__(self, id, name):
        self.__id = id
        self.__name = name
        self.__balance = 0
    
    # We provide just the getter method for the id 
    # because it is a read-only attribute
    @property
    def id(self):
        return self.__id
    
    # We provide both the getter and setter methods for the name
    # so that the name can be read and modified
    @property
    def name(self):
        return self.__name
    
    # We provide just the getter method for the balance
    # so the balance can only be modified through the deposit and withdraw methods
    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def balance(self):
        return self.__balance
    
    def withdraw(self, amount):
        if amount <= 0:
            print("Amount must be greater than 0")
            return
        if amount > self.balance:
            print("Insufficient funds")
            return
        self.__balance -= amount
        print(f"Withdrawal successful. Current balance: {self.balance}")
    
    def deposit(self, amount):
        if amount <= 0:
            print("Amount must be greater than 0")
            return
        self.__balance += amount
        print(f"Deposit successful. Current balance: {self.balance}")
    
    def show(self):
        print(f'ID: {self.id}, Name: {self.name}, Balance: {self.balance}')

### Test the Account class
acc01 = Account(1, "John")
acc01.deposit(100)
acc01.show()
acc01.withdraw(50)
acc01.show()