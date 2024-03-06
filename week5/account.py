from abc import ABC, abstractmethod

class Account(ABC):
    def __init__(self, id, name):
        self._id = id
        self._name = name
        self._balance = 0
    
    # We provide just the getter method for the id 
    # because it is a read-only attribute
    @property
    def id(self):
        return self._id
    
    # We provide both the getter and setter methods for the name
    # so that the name can be read and modified
    @property
    def name(self):
        return self._name
    
    # We provide just the getter method for the balance
    # so the balance can only be modified through the deposit and withdraw methods
    @name.setter
    def name(self, value):
        self._name = value

    @property
    def balance(self):
        return self._balance
    
    @abstractmethod
    def withdraw(self, amount):
        pass
    
    def deposit(self, amount):
        if amount <= 0:
            print("Amount must be greater than 0")
            return
        self._balance += amount
        print(f"Deposit successful. Current balance: {self.balance}")
    
    def __str__(self):
        return f'ID: {self.id}, Name: {self.name}, Balance: ${self.balance}'